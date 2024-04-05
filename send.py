#!/usr/bin/python3

import os, sys, json, requests
from datetime import datetime

SCRIPT_DIR = os.path.abspath(os.path.dirname(sys.argv[0]))
LOG_FILE = f'{SCRIPT_DIR}/loggers.log'

DEFAULT_NTFY_SERVER_URL = 'https://ntfy.sh'
DEFAULT_TIMEOUT_S = 10

def parse_args(args):
    # Keys for command line
    KEY_CLI_SERVER = '--server'
    KEY_CLI_TOPIC = '--topic'
    KEY_CLI_TITLE = '--title'
    KEY_CLI_MESSAGE = '--message'
    KEY_CLI_PRIORITY = '--priority'
    KEY_CLI_TAGS = '--tag'

    # Keys for request json body
    KEY_REQ_TOPIC = 'topic'
    KEY_REQ_TITLE = 'title'
    KEY_REQ_MESSAGE = 'message'
    KEY_REQ_PRIORITY = 'priority'
    KEY_REQ_TAGS = 'tags'

    parsed = {}
    has_topic = False
    server_url = None

    # Iterate over args
    for arg in args:
        # Get key and value parts of arg
        split = arg.strip().split('=')
        key = split[0]
        value = '='.join(split[1:])

        if key == KEY_CLI_SERVER:
            server_url = value
        elif key == KEY_CLI_TOPIC:
            # Topic, required
            has_topic = True
            parsed[KEY_REQ_TOPIC] = value
        elif key == KEY_CLI_TITLE:
            # Title
            parsed[KEY_REQ_TITLE] = value
        elif key == KEY_CLI_MESSAGE:
            # Message
            parsed[KEY_REQ_MESSAGE] = value
        elif key == KEY_CLI_PRIORITY:
            # Priority, integer
            parsed[KEY_REQ_PRIORITY] = int(value)
        elif key == KEY_CLI_TAGS:
            # Tags, list of values
            if KEY_REQ_TAGS not in parsed:
                parsed[KEY_REQ_TAGS] = []
            parsed[KEY_REQ_TAGS].append(value)
        else:
            raise Exception(f"Key '{key}' is not a valid key! (or it hasn't been implemented yet)")

    # Make sure topic is present
    if not has_topic:
        raise Exception(f"Key '{KEY_CLI_TOPIC}' is required but is missing!")

    return (server_url, parsed)

def log(message):
    # Current date and time
    now = datetime.now()
    date = f'{now.year}/{now.month:02}/{now.day:02} {now.hour:02}:{now.minute:02}:{now.second:02}'

    # Write to log
    with open(LOG_FILE, 'a') as f:
        f.write(f'{date} - {message}\n')

def send_json(data, server_url = DEFAULT_NTFY_SERVER_URL, timeout = DEFAULT_TIMEOUT_S):
    try:
        # Send POST request
        res = requests.post(server_url, data=json.dumps(data))
        
        # Check status
        if res.status_code != 200:
            raise Exception(f'Server responded with status code {res.status_code}')
    except Exception as e:
        raise Exception(f'Failed to send request: {e}')

if __name__ == '__main__':
    try:
        # CLI args containing the relevant bits
        args = sys.argv[1:]

        # Parse CLI args
        log(f'Parsing params: "{args}"')
        (server_url, data) = parse_args(args)

        # Send notification
        if server_url:
            # Custom URL
            log(f'Sending POST request to "{server_url}": "{data}"')
            send_json(data, server_url)
        else:
            # Default URL
            log(f'Sending POST request: "{data}"')
            send_json(data)

        log('Success!')
    except Exception as e:
        message = f'Error: Failed to send notification: {e}'

        log(message)
        print(message, file=os.sys.stderr)

        # Exit with error code
        exit(1)
