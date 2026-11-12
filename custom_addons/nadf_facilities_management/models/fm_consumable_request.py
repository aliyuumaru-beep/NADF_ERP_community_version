# Phase 2 — Process 1: Reactive Maintenance (Consumable / Material Request)
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class FmConsumableRequest(models.Model):
    """Materials request raised by a contractor against a Job Order or a
    Preventive Maintenance Schedule entry.

    Business purpose: lets a contractor draw consumables/spares needed to
    complete a job. Approval updates the contractor's tracked inventory
    (``fm.contractor.inventory.line``), which feeds the quarterly
    inventory report (Process 3).

    State machine: draft -> submitted -> approved/rejected.

    DECISION (Phase 7 — 7.2.4): originally limited to ``job_order_id``
    (Process 1 only). ``schedule_id`` is added so contractors can also draw
    materials against a Process 2 preventive maintenance entry. Exactly one
    of the two must be set (enforced by ``_check_source``); ``contractor_id``
    and ``branch_id`` are derived from whichever source is set.
    """
    _name = 'fm.consumable.request'
    _description = 'Consumable / Material Request for Job Order'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'fm.notification.mixin', 'fm.stock.mixin']
    _order = 'request_date desc, id desc'

    name = fields.Char(
        string='Reference', required=True, copy=False, readonly=True,
        default=lambda self: _('New'),
    )
    job_order_id = fields.Many2one(
        'fm.job.order', string='Job Order', ondelete='cascade', index=True,
    )
    schedule_id = fields.Many2one(
        'fm.maintenance.schedule', string='Maintenance Schedule Entry', ondelete='cascade', index=True,
    )
    contractor_id = fields.Many2one(
        'fm.contractor', string='Contractor', compute='_compute_source_fields',
        store=True, readonly=True,
    )
    branch_id = fields.Many2one(
        'hr.department', string='Branch', compute='_compute_source_fields',
        store=True, readonly=True,
    )
    request_date = fields.Datetime(string='Request Date', default=fields.Datetime.now)
    # Phase 7 — 7.2.4: DB-level backstop for _check_source below. The
    # @api.constrains only fires when job_order_id/schedule_id are present
    # in the write/create vals — a record created with neither field set at
    # all (e.g. a bare `create({'line_ids': [...]})`) would otherwise slip
    # through, so a CHECK constraint enforces the XOR unconditionally.
    _sql_constraints = [
        ('source_required',
         'CHECK ((job_order_id IS NOT NULL) != (schedule_id IS NOT NULL))',
         'A consumable request must be linked to exactly one of: a Job Order or a Maintenance Schedule entry.'),
    ]
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', tracking=True, copy=False)
    line_ids = fields.One2many('fm.consumable.request.line', 'request_id', string='Lines')
    desk_officer_notes = fields.Text(string='Desk Officer Notes')
    approved_by = fields.Many2one('res.users', string='Approved By', readonly=True, copy=False)
    approval_date = fields.Datetime(string='Approval Date', readonly=True, copy=False)
    issue_move_ids = fields.Many2many(
        'stock.move', 'fm_consumable_request_issue_move_rel', string='Stock Issued',
        readonly=True, copy=False, groups='stock.group_stock_user',
    )

    @api.depends(
        'job_order_id.contractor_id', 'job_order_id.branch_id',
        'schedule_id.contractor_id', 'schedule_id.plan_id.branch_id',
    )
    def _compute_source_fields(self):
        for rec in self:
            if rec.job_order_id:
                rec.contractor_id = rec.job_order_id.contractor_id
                rec.branch_id = rec.job_order_id.branch_id
            elif rec.schedule_id:
                rec.contractor_id = rec.schedule_id.contractor_id
                rec.branch_id = rec.schedule_id.plan_id.branch_id
            else:
                rec.contractor_id = False
                rec.branch_id = False

    @api.constrains('job_order_id', 'schedule_id')
    def _check_source(self):
        for rec in self:
            if bool(rec.job_order_id) == bool(rec.schedule_id):
                raise ValidationError(_(
                    'A consumable request must be linked to exactly one of: '
                    'a Job Order or a Maintenance Schedule entry.'
                ))

    @api.model
    def _fm_check_contractor(self):
        """Only the contractor doing the work requests consumables (sponsor
        directive, DEC-FM-003). The ACL already denies create to FM office
        roles; this gives a clear message and also covers Submit."""
        if not self.env.su and not self.env.user.has_group('nadf_facilities_management.group_fm_tff_contractor'):
            raise UserError(_('Only the contractor assigned to the job can request consumables. '
                              'Desk officers review and approve requests.'))

    @api.model_create_multi
    def create(self, vals_list):
        self._fm_check_contractor()
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('fm.consumable.request') or _('New')
        return super().create(vals_list)

    def action_submit(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError(_('Only draft consumable requests can be submitted.'))
            rec._fm_check_contractor()
            if not rec.line_ids:
                raise UserError(_('Add at least one consumable before submitting.'))
            for line in rec.line_ids.sudo():
                if line.quantity_requested <= 0:
                    raise UserError(_('Quantity requested must be greater than zero (%s).') % line.product_id.display_name)
                # Desk officer starts from the requested quantity and adjusts down if needed.
                line.quantity_approved = line.quantity_requested
            rec.write({'state': 'submitted'})
            rec.message_post(body=_('Consumable request submitted for approval.'))
            # Phase 6 — notify the Branch Desk Officer for approval.
            source_name = rec.job_order_id.name or rec.schedule_id.name
            desk_officers = rec._fm_branch_users(
                rec.branch_id, 'nadf_facilities_management.group_fm_branch_desk_officer',
            )
            for user in desk_officers:
                rec.activity_schedule(
                    'mail.mail_activity_data_todo',
                    summary=_('Consumable Request Awaiting Approval'),
                    note=_('Consumable request %s for %s is awaiting approval.') % (
                        rec.name, source_name,
                    ),
                    user_id=user.id,
                )
        return True

    def action_approve(self):
        inventory_model = self.env['fm.contractor.inventory.line']
        for rec in self:
            if rec.state != 'submitted':
                raise UserError(_('Only submitted consumable requests can be approved.'))
            for line in rec.line_ids:
                if line.quantity_approved < 0 or line.quantity_approved > line.quantity_requested:
                    raise UserError(_('Approved quantity for %s must be between 0 and the requested quantity.')
                                    % line.product_id.display_name)
            # DEC-FM-003: approval physically issues the parts from the
            # consumables store to the contractor's stock location.
            moves = rec._fm_move(
                [(l.product_id, l.quantity_approved) for l in rec.line_ids],
                rec._fm_issue_location(),
                rec.contractor_id._fm_get_stock_location(),
                rec.name,
            )
            rec.sudo().issue_move_ids = [(6, 0, moves.ids)]
            rec.write({
                'state': 'approved',
                'approved_by': self.env.user.id,
                'approval_date': fields.Datetime.now(),
            })
            for line in rec.line_ids:
                if not line.quantity_approved:
                    continue
                inventory_line = inventory_model.search([
                    ('contractor_id', '=', rec.contractor_id.id),
                    ('product_id', '=', line.product_id.id),
                ], limit=1)
                if inventory_line:
                    inventory_line.write({
                        'quantity_issued': inventory_line.quantity_issued + line.quantity_approved,
                        'last_updated': fields.Date.context_today(rec),
                    })
                else:
                    inventory_model.create({
                        'contractor_id': rec.contractor_id.id,
                        'product_id': line.product_id.id,
                        'quantity_issued': line.quantity_approved,
                        'uom_id': line.uom_id.id,
                        'last_updated': fields.Date.context_today(rec),
                    })
            rec.message_post(body=_('Consumable request approved — parts issued from %(src)s to the contractor.') % {
                'src': rec._fm_issue_location().display_name})
            for user in rec.contractor_id.user_ids:
                rec.sudo().activity_schedule(
                    'mail.mail_activity_data_todo',
                    summary=_('Consumables approved — collect and complete the job'),
                    note=_('Consumable request %s was approved. Record the quantities you use on the request before submitting your completion report.') % rec.name,
                    user_id=user.id,
                )
            # Phase 6 — notify the contractor by email.
            rec._fm_send_template(
                'nadf_facilities_management.mail_template_fm_consumable_request_approved', rec.id,
            )
        return True

    def action_reject(self):
        for rec in self:
            if rec.state != 'submitted':
                raise UserError(_('Only submitted consumable requests can be rejected.'))
            rec.write({'state': 'rejected'})
            rec.message_post(body=_('Consumable request rejected.'))
        return True


class FmConsumableRequestLine(models.Model):
    """Single product line on a Consumable Request, with planned vs.
    approved quantity and the resulting cost."""
    _name = 'fm.consumable.request.line'
    _description = 'Consumable / Material Request Line'

    request_id = fields.Many2one(
        'fm.consumable.request', string='Request', required=True, ondelete='cascade', index=True,
    )
    product_id = fields.Many2one(
        'product.product', string='Consumable', required=True,
        domain="[('fm_consumable', '=', True)]",
    )
    description = fields.Char(string='Description')
    quantity_requested = fields.Float(string='Quantity Requested', required=True, default=1.0)
    quantity_approved = fields.Float(string='Quantity Approved')
    # DEC-FM-003: what the contractor actually used on the job; posted out of
    # the contractor's stock when the completion report is submitted.
    quantity_consumed = fields.Float(string='Quantity Used')
    consumption_posted = fields.Boolean(string='Usage Posted', readonly=True, copy=False)
    qty_in_store = fields.Float(
        string='In Store', compute='_compute_qty_in_store',
        help='Quantity currently available in the Facilities consumables store.',
    )
    request_state = fields.Selection(related='request_id.state', string='Request Status')
    uom_id = fields.Many2one(
        'uom.uom', string='Unit of Measure', related='product_id.uom_id', store=True, readonly=True,
    )
    unit_cost = fields.Float(string='Unit Cost', readonly=True)
    total_cost = fields.Float(string='Total Cost', compute='_compute_total_cost', store=True)

    # Fields only the Branch Desk Officer (or system) may set.
    _FM_OFFICER_FIELDS = {'quantity_approved', 'unit_cost'}

    @api.depends('product_id')
    def _compute_qty_in_store(self):
        store = self.env['fm.consumable.request']._fm_issue_location()
        for rec in self:
            rec.qty_in_store = rec.product_id and self.env['fm.consumable.request']._fm_qty_at(rec.product_id, store) or 0.0

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.unit_cost = self.product_id.standard_price
            if not self.description:
                self.description = self.product_id.name

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('product_id') and not vals.get('unit_cost'):
                vals['unit_cost'] = self.env['product.product'].browse(vals['product_id']).standard_price
        lines = super().create(vals_list)
        lines._fm_check_edit_rights(set().union(*[set(v) for v in vals_list]) if vals_list else set(), creating=True)
        return lines

    def write(self, vals):
        self._fm_check_edit_rights(set(vals))
        if 'product_id' in vals and 'unit_cost' not in vals:
            vals['unit_cost'] = self.env['product.product'].browse(vals['product_id']).standard_price
        return super().write(vals)

    def _fm_check_edit_rights(self, fields_set, creating=False):
        if self.env.su:
            return
        is_officer = self.env.user.has_group('nadf_facilities_management.group_fm_branch_desk_officer')
        for line in self:
            state = line.request_id.state
            if fields_set & {'product_id', 'quantity_requested'} and state != 'draft':
                raise UserError(_('Consumables and requested quantities can only be changed while the request is in Draft.'))
            if not creating and fields_set & self._FM_OFFICER_FIELDS and not is_officer:
                raise UserError(_('Only the Branch Desk Officer can set approved quantities or costs.'))
            if 'quantity_approved' in fields_set and not creating and state != 'submitted':
                raise UserError(_('Approved quantities can only be changed while the request is awaiting approval.'))
            if 'quantity_consumed' in fields_set:
                if state != 'approved' or line.consumption_posted:
                    raise UserError(_('Quantities used can only be recorded on an approved request before the completion report is submitted.'))

    @api.constrains('quantity_consumed', 'quantity_approved')
    def _check_quantity_consumed(self):
        for line in self:
            if line.quantity_consumed < 0 or line.quantity_consumed > line.quantity_approved:
                raise ValidationError(_('Quantity used for %(p)s cannot exceed the approved quantity (%(q)s).') % {
                    'p': line.product_id.display_name, 'q': line.quantity_approved})

    @api.depends('quantity_approved', 'unit_cost')
    def _compute_total_cost(self):
        for rec in self:
            rec.total_cost = rec.quantity_approved * rec.unit_cost
