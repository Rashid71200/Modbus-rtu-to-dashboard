import socket
from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO

import random

FORMAT = 'utf-8'
host = socket.gethostbyname(socket.gethostname())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, 5050))

app = Flask(__name__)
app.config["SECRET_KEY"] = "ahrneloy"
socketio = SocketIO(app)

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("styledashboard.html")

@socketio.on("update_value")
def update_value():
    global value
    message = '{}'.format("frequencyValue")
    client.send(message.encode(FORMAT))

    value = client.recv(1024).decode(FORMAT)


    socketio.emit("update_value", {"value": value})

if __name__ == "__main__":
    socketio.run(app, debug=True)