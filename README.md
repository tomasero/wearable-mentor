# Wearable Mentor

---

### Architecture

- Mobile App
  - Stream data from wearable, parse it to text, and send it to server
- Wearable
  - Comfortable wearable with microphone and speaker
- Server
  - Listens to app, analyzes microphone data, and sends back advice/mentorship

### Server

Path to server is

    /server/server.py

To run

    cd server
    python server.py

To test from CLI

    curl -X POST --data "arg1=raptor" --data "arg2=t-rex" http://localhost:5001/args 
