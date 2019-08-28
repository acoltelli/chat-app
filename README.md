# chat-app

Chat app with barebones front end, allows user to choose a username and join an already existing chatroom or create their own channel. Channels will display the last 100 messages sent with timestamp and user info. Users can also see their message history across all channels in their profile. 


## Stack
This project is built using a Flask and [Socket.IO](https://socket.io/), a javascript library which enables realtime communication between web clients and servers using the [WebSocket](https://en.wikipedia.org/wiki/WebSocket) protocol.

## Build Instructions

Create .env file in project. Copy and paste the following.  
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


