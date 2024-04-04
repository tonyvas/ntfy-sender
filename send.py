#!/usr/bin/python3

import os, sys, json, requests
from datetime import datetime

SCRIPT_DIR = os.path.abspath(os.path.dirname(sys.argv[0]))
LOG_FILE = f'{SCRIPT_DIR}/loggers.log'

NTFY_SERVER_URL='https://ntfy.sh'
DEFAULT_TIMEOUT_S = 10

def parse_args(args):
    KEYS_TOPIC = 'topic'
    KEYS_TITLE = 'title'
    KEYS_MESSAGE = 'message'
    KEYS_PRIORITY = 'priority'
    KEYS_TAG = 'tag'
    KEYS_TAGS = 'tags'

    parsed = {}
    has_topic = False

    # Iterate over args
    for arg in args:
        # Get key and value parts of arg
        split = arg.strip().split('=')
        key = split[0]
        value = '='.join(split[1:])

        if key == KEYS_TOPIC:
            # Topic is required
            has_topic = True
            parsed[key] = value
        elif key in [ KEYS_TITLE, KEYS_MESSAGE ]:
            # Regular strings
            parsed[key] = value
        elif key == KEYS_PRIORITY:
            # Int value
            parsed[key] = int(value)
        elif key == KEYS_TAG:
            # List of values
            if key not in parsed:
                parsed[key] = []
            parsed[key].append(key)
        else:
            raise Exception(f"Key '{key}' is not a valid key! (or it hasn't been implemented yet)")

    # Make sure topic is present
    if not has_topic:
        raise Exception(f"Key '{KEYS_TOPIC}' is required but is missing!")

    return parsed

def log(message):
    # Current date and time
    now = datetime.now()
    date = f'{now.year}/{now.month:02}/{now.day:02} {now.hour:02}:{now.minute:02}:{now.second:02}'

    # Write to log
    with open(LOG_FILE, 'a') as f:
        f.write(f'{date} - {message}\n')

def send_json(data, timeout = DEFAULT_TIMEOUT_S):
    try:
        # Send POST request
        res = requests.post(NTFY_SERVER_URL, data=json.dumps(data))
        
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
        params = parse_args(args)

        # Send notification
        log(f'Sending POST request: "{params}"')
        send_json(params)

        log('Success!')
    except Exception as e:
        message = f'Error: Failed to send notification: {e}'

        log(message)
        print(message, file=os.sys.stderr)

        # Exit with error code
        exit(1)