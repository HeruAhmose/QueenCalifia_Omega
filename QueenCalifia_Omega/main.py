
from flask import Flask, render_template, request, jsonify
from drive_sync import upload_to_drive
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ QueenCalifia-Ω is online. Visit /dashboard"

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.json
    with open("log/interactions.log", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {data}\n")
    return jsonify({"status": "🧠 Ingested and logged."})

@app.route('/sync')
def sync():
    result = upload_to_drive("log/interactions.log")
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
