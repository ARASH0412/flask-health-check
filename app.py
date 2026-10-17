from flask import Flask, jsonify, render_template
from datetime import datetime, timezone
import time

app = Flask(__name__)
start_time = time.time()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "application": "Flask Health App",
        "version": "1.0",
        "status": "healthy",
        "uptime_seconds": int(time.time() - start_time),
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)