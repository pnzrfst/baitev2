#!/usr/bin/env bash
TEAL=$'\033[38;5;79m'
BLACK=$'\033[38;5;232m'
BLUE=$'\033[38;5;33m'
DIM=$'\033[2;38;5;245m'
RESET=$'\033[0m'
BOLD=$'\033[1m'

visible() { sed 's/\x1b\[[0-9;]*m//g' <<< "$1"; }

lines=(
    "${BOLD}${TEAL}████   ███  █████ █████ █████"
    "█   █ █   █   █     █   █"
    "█   █ █   █   █     █   █"
    "████  █████   █     █   ████"
    "█   █ █   █   █     █   █"
    "█   █ █   █   █     █   █"
    "████  █   █ █████   █   █████${RESET}"
    ""
    ""
    ""
    "${TEAL}       ██████"
    "     ████████████"
    "   ████████████████████"
    "  ${TEAL}██████████████████████${TEAL}██████"
    "  ${TEAL}██████${BLACK}██${TEAL}████████████${BLACK}██${TEAL}██████"
    "  ████████████████████████████"
    "   ████████████    ██████████"
    "     ██████████  ████████"
    "   ████    ██████   ████${RESET}"
    ""
    ""
    ""
    "${DIM}        watching your clipboard...${RESET}"
)

cols=$(tput cols 2>/dev/null || echo 80)

max_width=0
for line in "${lines[@]}"; do
    vis=$(visible "$line")
    length=${#vis}
    (( length > max_width )) && max_width=$length
done

for line in "${lines[@]}"; do
    if [[ -z "$(visible "$line")" ]]; then
        printf '\n'
        continue
    fi
    vis=$(visible "$line")
    length=${#vis}
    pad=$(( (cols - max_width) / 2 + (max_width - length) ))
    (( pad < 0 )) && pad=0
    printf '%*s%s\n' "$pad" "" "$line"
done