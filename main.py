from flask import Flask, send_file, render_template, request
import subprocess
import os
from dotenv import load_dotenv
import pymongo
from bson.json_util import dumps
import json
import pandas

client = pymongo.MongoClient("localhost",27017)
db = client["madsat"]
eventsCollection = db["events"]

load_dotenv()

PATH = os.getenv("madsat-path")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/events")
def events():
    format = request.args.get("format")
    if format == "csv":
        events = eventsCollection.find()
        json_string = dumps(events)
        df = pandas.read_json(json_string)
        return df.to_csv()
    else:
        events = eventsCollection.find()
        json_string = dumps(events)
        return json.loads(json_string)

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