#  Event Scheduler System

This is a backend application built with Python and Flask that allows users to schedule, update, delete, and list events. Events are stored in a JSON file so they persist even after restarting the server.


# Features

- Create a new event
- View all scheduled events
- Search events by title or description
- Update an existing event
- Delete an event
- Events are persisted in `events.json`


# Requirements

- Python 3.x
- Flask

Install dependencies:
```bash
pip install -r requirements.txt
```

---

# How to Run the App

```bash
python app.py
```
The app will start at: `http://127.0.0.1:5000/`

---

## 📮 API Endpoints

### ➕ Create Event
`POST /events`
```json
{
  "title": "Doctor Appointment",
  "description": "Visit Dr. Smith",
  "start_time": "2025-06-29T10:00:00",
  "end_time": "2025-06-29T11:00:00"
}
```

### 📋 Get All Events
`GET /events`
- Sorted by start_time ascending
- Optional search: `GET /events?q=doctor`

### ✏️ Update Event
`PUT /events/<event_id>`
```json
{
  "title": "Updated Meeting Title"
}
```

### ❌ Delete Event
`DELETE /events/<event_id>`

---

## 🧪 Testing with Postman

1. Import the provided `postman_collection.json` (create it manually or request it from developer)
2. Test all routes: create, get, update, delete

---

## 📁 File Structure
```
event_scheduler/
├── app.py              # Flask app
├── storage.py          # File read/write helpers
├── events.json         # Data store (auto-generated)
├── requirements.txt    # Python dependencies
└── README.md           # Project guide
```