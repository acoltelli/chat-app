# chat-app

Chat app with barebones front end, allows user to choose a username and join an already existing chatroom or create their own channel. Channels will display the last 100 messages sent with timestamp and user info. Users can also see their message history across all channels in their profile.


## Stack
This project is built using Flask and [Socket.IO](https://socket.io/), a javascript library which enables realtime communication between web clients and servers using the [WebSocket](https://en.wikipedia.org/wiki/WebSocket) protocol. Message history is currently stored locally but migration to a database is trivial with Flask.

## Build Instructions

Create .env file in project. Copy and paste the following choosing your own secret key.
```
export FLASK_APP = application.py
export SECRET_KEY = '<some-secret-key>'

```
cd into project
```javascript
// Install all dependencies
pip3 install -r requirements.txt

// Run application
flask run

// Project builds at http://localhost:5000
