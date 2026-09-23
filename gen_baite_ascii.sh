#!/usr/bin/env bash
TEAL=$'\033[38;5;79m'
BLACK=$'\033[38;5;232m'
BLUE=$'\033[38;5;33m'
DIM=$'\033[2;38;5;245m'
RESET=$'\033[0m'
BOLD=$'\033[1m'

{
printf '%s' "$BOLD$TEAL"
cat << 'WORD'
████   ███  █████ █████ █████
█   █ █   █   █     █   █
█   █ █   █   █     █   █
████  █████   █     █   ████
█   █ █   █   █     █   █
█   █ █   █   █     █   █
████  █   █ █████   █   █████
WORD
printf '%s\n\n\n' "$RESET"

printf '%s' "$TEAL"
printf '       ██████\n'
printf '     ████████████\n'
printf '   ████████████████████\n'

# body row with blue square above right eye
printf '  '; printf '%s████████████████████%s██%s██████\n' "$TEAL" "$TEAL" "$TEAL"

# eyes row, fully solid, no gaps
printf '  '; printf '%s██████%s██%s████████████%s██%s██████\n' "$TEAL" "$BLACK" "$TEAL" "$BLACK" "$TEAL"

printf '%s' "$TEAL"
printf '  ████████████████████████████\n'
printf '   ████████████    ██████████\n'
printf '     ██████████  ████████\n'
printf '   ████    ██████   ████\n'
printf '%s\n\n\n' "$RESET"

printf '%s        watching your clipboard...%s\n' "$DIM" "$RESET"
}
