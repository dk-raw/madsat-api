from flask import Flask, send_file, render_template
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

PATH = os.getenv("madsat-path")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/events")
def events():
    return send_file(f"{PATH}/events.txt", mimetype="text/plain")

@app.route("/logs")
def logs():
    return send_file(f"{PATH}/liggma.log", mimetype="text/plain")

@app.route("/status")
def status():
    status = subprocess.call(["systemctl", "is-active", "--quiet", "madsat.service"])
    if status == 0:
        return "ACTIVE"
    else:
        return "INACTIVE"


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=9000)