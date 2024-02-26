from flask import Flask, jsonify, send_from_directory
import json
from mongita import MongitaClientDisk

# create Mongita client connection
client = MongitaClientDisk()

# open movie database
movie_db = client.movie_db

# open a sci fi collection
sci_fi_collection = movie_db.sci_fi_collection

app = Flask(__name__)

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/')
def serve_index():
    return send_from_directory('.',"index.html")

@app.route("/data/movies/scifi")
def get_data_movies_scifi():
    #with open("classic_sci_fi_movies.json","r") as f:
    #    data = json.load(f)
    data = list(sci_fi_collection.find({}))
    for item in data:
        del item["_id"]
    return jsonify(data)

@app.route("/api/status")
def get_status():
    data = [
        {"name":"suzie","status":"fine"},
        {"name":"cindy","status":"sad"},
        {"name":"meg","status":"lame"}
    ]
    return jsonify(data)