#!/usr/bin/env bash
# Project-level bootstrap (SPEC-GOV-ENF-001 layer L2).
# If the governance gateway is installed for this user, the user-level hooks do the work: exit quietly.
# If not, block every write so nobody can work on this repo un-governed.
GOV="${GOV_HOME:-$HOME/.claude/governance}/govcore.py"
[ -f "$GOV" ] && exit 0
EVENT="$1"
MSG="Software Factory governance gateway is NOT installed on this machine, so work on this repository is blocked. Ask the user to run: git clone https://github.com/aliyuumaru-beep/software-factory-governance && bash software-factory-governance/enforcement/install.sh   (then restart Claude Code). See AGENTS.md."
if [ "$EVENT" = "SessionStart" ]; then
  python3 -c 'import json,sys; print(json.dumps({"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":sys.argv[1]}}))' "$MSG"
  exit 0
fi
INPUT=$(cat)
TOOL=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_name",""))' 2>/dev/null)
if [ "$TOOL" = "Bash" ]; then
  CMD=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null)
  case "$CMD" in
    *install.sh*|git\ clone*|ls*|cat*|head*|tail*|grep*|git\ status*|git\ log*|git\ diff*|git\ show*) exit 0 ;;
  esac
fi
python3 -c 'import json,sys; print(json.dumps({"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":sys.argv[1]}}))' "$MSG"
exit 0
