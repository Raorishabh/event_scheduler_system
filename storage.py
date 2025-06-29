import json
import os

FILE_NAME = 'events.json'

def load_events():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_events(events):
    with open(FILE_NAME, 'w') as f:
        json.dump(events, f, indent=4)
