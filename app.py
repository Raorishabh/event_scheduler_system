from flask import Flask, jsonify, request
from uuid import uuid4
import json
from storage import load_events, save_events

app = Flask(__name__)
events = load_events()

# Sort events by start time
def sort_events():
    return sorted(events.values(), key=lambda e: e['start_time'])

# Create a new event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    required = ['title', 'description', 'start_time', 'end_time']
    if not all(field in data for field in required):
        return jsonify({'error': 'Missing fields'}), 400

    event_id = str(uuid4())
    event = {
        'id': event_id,
        'title': data['title'],
        'description': data['description'],
        'start_time': data['start_time'],
        'end_time': data['end_time']
    }
    events[event_id] = event
    save_events(events)
    return jsonify(event), 201

# Get all events (sorted and optionally filtered)
@app.route('/events', methods=['GET'])
def list_events():
    query = request.args.get('q')
    sorted_events = sort_events()
    if query:
        filtered = [e for e in sorted_events if query.lower() in e['title'].lower() or query.lower() in e['description'].lower()]
        return jsonify(filtered)
    return jsonify(sorted_events)

# Update an existing event
@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    if event_id not in events:
        return jsonify({'error': 'Event not found'}), 404
    data = request.get_json()
    events[event_id].update({k: v for k, v in data.items() if k in ['title', 'description', 'start_time', 'end_time']})
    save_events(events)
    return jsonify(events[event_id])

# Delete an event
@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    if event_id not in events:
        return jsonify({'error': 'Event not found'}), 404
    deleted = events.pop(event_id)
    save_events(events)
    return jsonify(deleted)

if __name__ == '__main__':
    app.run(debug=True)
