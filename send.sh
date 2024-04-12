#!/usr/bin/bash

# Change these values where needed
SERVER_URL="https://ntfy.sh"                    # The URL of where NTFY is hosted
NTFY_SENDER_SCRIPT="/opt/ntfy-sender/send.py"   # The path where the ntfy-sender script is stored
DEFAULT_TOPIC="J8C5bROgvOPoqlmW"                # The default topic
DEFAULT_TITLE="Default Title"                   # The default title
DEFAULT_MESSAGE="Default message"               # The default message
DEFAULT_PRIORITY=3                              # The default priority

# Where to log notifications
SCRIPT_DIR=$(dirname "$0")
LOG_FILE="${SCRIPT_DIR}/notifications.log"

# Override values from commandline
topic=${1:-"${DEFAULT_TOPIC}"}
title=${2:-"${DEFAULT_TITLE}"}
message=${3:-"${DEFAULT_MESSAGE}"}
priority=${4:-"${DEFAULT_PRIORITY}"}

# Log message
log_message="$(date '+%F %T')"
log_message+=$'\n\t'"Topic:    ${topic}"
log_message+=$'\n\t'"Title:    ${title}"
log_message+=$'\n\t'"Message:  ${message}"
log_message+=$'\n\t'"Priority: ${priority}"

echo "${log_message}"$'\n' >> "${LOG_FILE}"

# Send message
"${NTFY_SENDER_SCRIPT}" \
    --server="${SERVER_URL}" \
    --topic="${topic}" \
    --title="${title}" \
    --message="${message}" \
    --priority=${priority}