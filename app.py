from pathlib import Path
import os
import sqlite3
from datetime import datetime, timezone
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
DB = Path(__file__).with_name("abyss_run.db")

def connect():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with connect() as db:
        db.execute("""CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player TEXT NOT NULL,
            score INTEGER NOT NULL,
            depth INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )""")
        db.commit()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/health")
def health():
    return jsonify(game="ABYSS RUN", status="online")

@app.route("/api/scores", methods=["GET"])
def get_scores():
    with connect() as db:
        rows = db.execute(
            "SELECT player,score,depth,created_at FROM scores ORDER BY score DESC LIMIT 10"
        ).fetchall()
    return jsonify([dict(row) for row in rows])

@app.route("/api/scores", methods=["POST"])
def save_score():
    data = request.get_json(silent=True) or {}
    try:
        player = str(data.get("player", "DIVER")).strip()[:18] or "DIVER"
        score = max(0, min(int(data.get("score", 0)), 10_000_000))
        depth = max(0, min(int(data.get("depth", 0)), 100_000))
    except (TypeError, ValueError):
        return jsonify(error="Score and depth must be numbers"), 400

    with connect() as db:
        db.execute(
            "INSERT INTO scores(player,score,depth,created_at) VALUES(?,?,?,?)",
            (player, score, depth, datetime.now(timezone.utc).isoformat())
        )
        db.commit()
    return jsonify(saved=True)

# Gunicorn imports this module, so initialize the database at startup too.
init_db()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "5000")),
        debug=False
    )
