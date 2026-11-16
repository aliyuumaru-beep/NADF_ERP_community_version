# DEC-FM-003 — Facilities consumables held as real inventory.
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    fm_consumable = fields.Boolean(
        string='Facilities Consumable',
        help='Spare part or consumable that maintenance contractors can request '
             'on Facilities Management consumable requests.',
    )


class FmContractor(models.Model):
    _inherit = 'fm.contractor'

    stock_location_id = fields.Many2one(
        'stock.location', string='Contractor Stock Location', readonly=True, copy=False,
        help='Parts issued to this contractor and not yet consumed are held here.',
    )

    def _fm_get_stock_location(self):
        """Return (creating on first use) this contractor's stock location."""
        self.ensure_one()
        if not self.stock_location_id:
            parent = self.env.ref('nadf_facilities_management.fm_location_contractor_stock')
            self.sudo().stock_location_id = self.env['stock.location'].sudo().create({
                'name': self.name,
                'usage': 'internal',
                'location_id': parent.id,
            })
        return self.stock_location_id


class FmStockMixin(models.AbstractModel):
    """Stock helpers shared by consumable requests and job orders.

    Stock moves are done with sudo(): desk officers and contractors are not
    Inventory users. The FM workflow itself (state checks, record rules on
    the FM documents) decides who may trigger a move.
    """
    _name = 'fm.stock.mixin'
    _description = 'Facilities Management stock helpers'

    @api.model
    def _fm_issue_location(self):
        """Store parts are issued from: system parameter override, else the
        warehouse's 'Consumables Store', else the warehouse stock location."""
        Location = self.env['stock.location'].sudo()
        param = self.env['ir.config_parameter'].sudo().get_param('nadf_fm.issue_location_id')
        if param and Location.browse(int(param)).exists():
            return Location.browse(int(param))
        warehouse = self.env['stock.warehouse'].sudo().search(
            [('company_id', '=', self.env.company.id)], limit=1)
        store = Location.search([
            ('name', '=', 'Consumables Store'), ('usage', '=', 'internal'),
            ('location_id', '=', warehouse.view_location_id.id),
        ], limit=1)
        return store or warehouse.lot_stock_id

    @api.model
    def _fm_qty_at(self, product, location):
        return product.sudo().with_context(location=location.id).qty_available

    @api.model
    def _fm_move(self, lines, source, dest, reference):
        """Move ``lines`` [(product, qty)] from ``source`` to ``dest`` and
        validate immediately. Raises if ``source`` lacks stock."""
        lines = [(p, q) for p, q in lines if q > 0]
        if not lines:
            return self.env['stock.move']
        short = [
            _('%(product)s: need %(need)s, available %(avail)s') % {
                'product': p.display_name, 'need': q, 'avail': self._fm_qty_at(p, source)}
            for p, q in lines
            if p.detailed_type == 'product' and self._fm_qty_at(p, source) < q
        ]
        if short:
            raise UserError(_('Not enough stock in %(loc)s:\n%(lines)s') % {
                'loc': source.display_name, 'lines': '\n'.join(short)})
        Move = self.env['stock.move'].sudo()
        moves = Move.create([{
            'name': reference,
            'reference': reference,
            'origin': reference,
            'product_id': p.id,
            'product_uom': p.uom_id.id,
            'product_uom_qty': q,
            'location_id': source.id,
            'location_dest_id': dest.id,
            'company_id': self.env.company.id,
        } for p, q in lines])
        moves._action_confirm()
        moves._action_assign()
        for move in moves:
            move.quantity = move.product_uom_qty
            move.picked = True
        moves._action_done()
        return moves
