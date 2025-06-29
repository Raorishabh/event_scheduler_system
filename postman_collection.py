{
  "info": {
    "_postman_id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "name": "Event Scheduler Collection",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Create Event",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"title\": \"Doctor Appointment\",\n  \"description\": \"Visit Dr. Smith\",\n  \"start_time\": \"2025-06-29T10:00:00\",\n  \"end_time\": \"2025-06-29T11:00:00\"\n}"
        },
        "url": {
          "raw": "http://localhost:5000/events",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["events"]
        }
      }
    },
    {
      "name": "List Events",
      "request": {
        "method": "GET",
        "url": {
          "raw": "http://localhost:5000/events",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["events"]
        }
      }
    },
    {
      "name": "Search Events",
      "request": {
        "method": "GET",
        "url": {
          "raw": "http://localhost:5000/events?q=doctor",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["events"],
          "query": [
            {
              "key": "q",
              "value": "doctor"
            }
          ]
        }
      }
    },
    {
      "name": "Update Event",
      "request": {
        "method": "PUT",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"title\": \"Updated Event Title\"\n}"
        },
        "url": {
          "raw": "http://localhost:5000/events/<event_id>",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["events", "<event_id>"]
        }
      }
    },
    {
      "name": "Delete Event",
      "request": {
        "method": "DELETE",
        "url": {
          "raw": "http://localhost:5000/events/<event_id>",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["events", "<event_id>"]
        }
      }
    }
  ]
}
