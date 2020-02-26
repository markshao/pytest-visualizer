from pathlib import Path
from threading import Lock
import random
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

CURRENT_PATH = Path(__file__)
TEMPLATE_FOLDER = CURRENT_PATH.parents[2].joinpath("vapp", "templates")
STATIC_FOLDER = CURRENT_PATH.parents[2].joinpath("vapp", "tempates")

app = Flask(__name__,
            static_url_path="",
            static_folder=STATIC_FOLDER,
            template_folder=TEMPLATE_FOLDER)
app.config["SECRET_KEY"] = "secret"

socketio = SocketIO(app)
thread = None
thread_lock = Lock()


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on('my_event', namespace='/test')
def test_message(message):
    emit('my_response', {'data': message['data']})


@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


def background_thread():
    while True:
        socketio.sleep(5)
        t = random.randint(1, 100)
        socketio.emit('my_response',
                      {'data': t}, namespace='/test')


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == "__main__":
    socketio.run(app)
