from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route("/")
def get_index():
    me = "Steve D."
    return f"<p>Hello, {me} from the World!</p>"

@app.route("/goodbye")
def get_goodbye():
    return "<p>Goodbye, world!</p>"

@app.route("/data")
def get_data():
    data = [
        {"name":"suzy","type":"dog"},
        {"name":"cindy","type":"cat"}
    ]
    return jsonify(data)

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route("/api/status")
def get_status():
    data = [
        {"name":"suzie","status":"fine"},
        {"name":"cindy","status":"sad"},
        {"name":"meg","status":"lame"}
    ]
    return jsonify(data)

@app.route("/whatever")
def get_whatever():
    return f"<p>Whatever, man</p>"