#!/usr/bin/env bash
# Project-level bootstrap (SPEC-GOV-ENF-001 layer L2).
# If the governance gateway is installed for this user, the user-level hooks do the work: exit quietly.
# If not, block every write so nobody can work on this repo un-governed. Only a short list of
# single, read-only commands (or the gateway install itself) is let through. Compound commands
# (; & | ` $( > <) are always blocked, so `ls && rm -rf x` cannot slip past.
GOV="${GOV_HOME:-$HOME/.claude/governance}/govcore.py"
[ -f "$GOV" ] && exit 0
EVENT="$1"
MSG="Software Factory governance gateway is NOT installed on this machine, so work on this repository is blocked. Ask the user to run: git clone https://github.com/aliyuumaru-beep/software-factory-governance && bash software-factory-governance/enforcement/install.sh   (then restart Claude Code). See AGENTS.md."
emit() { python3 -c 'import json,sys; print(json.dumps({"hookSpecificOutput":{"hookEventName":sys.argv[1],sys.argv[2]:sys.argv[3]} | ({"permissionDecisionReason":sys.argv[4]} if len(sys.argv)>4 else {})}))' "$@"; }
if [ "$EVENT" = "SessionStart" ]; then
  emit SessionStart additionalContext "$MSG"
  exit 0
fi
INPUT=$(cat)
TOOL=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_name",""))' 2>/dev/null)
if [ "$TOOL" = "Bash" ]; then
  CMD=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; print((json.load(sys.stdin).get("tool_input") or {}).get("command",""))' 2>/dev/null)
  case "$CMD" in
    *";"*|*"&"*|*"|"*|*'`'*|*'$('*|*">"*|*"<"*|*$'\n'*) ;;   # compound/redirect: fall through to deny
    *)
      FIRST=${CMD%% *}
      case "$FIRST" in
        ls|cat|head|tail|grep|pwd|wc) exit 0 ;;
        git)
          SUB=$(printf '%s' "$CMD" | awk '{print $2}')
          case "$SUB" in status|log|diff|show|clone) exit 0 ;; esac ;;
        bash)
          case "$CMD" in "bash "*software-factory-governance/enforcement/install.sh*) exit 0 ;; esac ;;
      esac ;;
  esac
fi
emit PreToolUse permissionDecision deny "$MSG"
exit 0
