from pathlib import Path
from flask import Flask, render_template
from flask_socketio import SocketIO

CURRENT_PATH = Path(__file__)
TEMPLATE_FOLDER = CURRENT_PATH.parents[2].joinpath("vapp", "templates")
STATIC_FOLDER = CURRENT_PATH.parents[2].joinpath("vapp", "tempates")

app = Flask(__name__,
            static_url_path="",
            static_folder=STATIC_FOLDER,
            template_folder=TEMPLATE_FOLDER)
app.config["SECRET_KEY"] = "secret"
socketio = SocketIO(app)


@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app)
