import os
import datetime
from flask import Flask, flash, render_template, redirect, jsonify, request, url_for, session
from flask_socketio import SocketIO, emit, send, emit, join_room, leave_room
from flask_session import Session
from forms import *


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

ROOMS = ['general']
channel_data = {'general':[]}

def cullList(room):
	data = channel_data[room]
	if len(data) > 100:
		data.pop(0)

@app.route('/', methods=['GET', 'POST'])
def index():
	if 'name' in session:
		form = CreateChannel()
		name = session['name']
		session.pop('room', None)
		# Create new channel
		if form.validate_on_submit():
			if form.room.data not in ROOMS:
				ROOMS.append(form.room.data)
				channel_data[form.room.data] = []
				session['room'] = form.room.data
				# Upon creation of new channel, user joins that channel
				return redirect(url_for('.chat'))
			flash('That channel already exists', 'danger')
	else:
		form = LoginForm()
		name = None
		if form.validate_on_submit():
			session['name'] = form.name.data
			# User automatically joins the 'general' room after creation of display name
			session['room'] = 'general'
			return redirect(url_for('.chat'))
	return render_template('index.html', form=form, name=name, rooms=ROOMS)

# helper function to update session variable onclick
# TODO: ideally this would be done with ajax
@app.route('/helper/<foo>')
def helper(foo):
	session['room'] = foo
	return redirect(url_for('.chat'))

@app.route('/chat')
def chat():
	name = session.get('name', '')
	room = session.get('room', '')
	# You would have to do weird things to see this error, keeping it in case there is an overlooked bug
	if name == '' or room == '':
		flash('Error!', 'danger')
		return redirect(url_for('.index'))
	return render_template('chat.html', name=name, room=room, data=channel_data[room])

@app.route('/account/<name>')
def account(name):
	return render_template('account.html', name=name, data=list(channel_data.values()))

@socketio.on('joined', namespace='/chat')
def joined(message):
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the channel'}, room=room)

@socketio.on('text', namespace='/chat')
def text(message):
	room = session.get('room')
	time = '{:%H:%M:%S}'.format(datetime.datetime.now())
	emit('message', {'msg': session.get('name') + ' @ ' + time + ' : ' + message['msg']}, room=room)
	channel_data[room].append([session.get('name'), time, message['msg'], room])
	# TODO: come up with a more efficient way to limit length of list so dont have to call after every append
	cullList(room)

@socketio.on('left', namespace='/chat')
def left(message):
	room = session.get('room')
	leave_room(room)
	emit('status', {'msg': session.get('name') + ' has left the channel'}, room=room)
