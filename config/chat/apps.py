from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(f"{username} joined {room}", to=room)

@socketio.on('message')
def handle_message(data):
    send(data['msg'], to=data['room'])

@socketio.on('leave')
def on_leave(data):
    leave_room(data['room'])
    send(f"{data['username']} left the room", to=data['room'])

if __name__ == '__main__':
    socketio.run(app, debug=True)