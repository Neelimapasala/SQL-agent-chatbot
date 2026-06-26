"""
app.py — Flask server that exposes the SQL agent via REST API
"""
import os
import webbrowser
from threading import Timer

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from agent import build_agent, run_query

load_dotenv()

app = Flask(__name__, static_folder="static")
CORS(app)

# Build the agent once at startup
print("🔧 Initializing SQL Agent...")
agent = build_agent()
print("✅ SQL Agent ready!")


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    model = data.get("model")  # currently informational; wire into agent.py if you want per-request model switching

    if not question:
        return jsonify({"error": "Question cannot be empty."}), 400

    if len(question) > 600:
        return jsonify({"error": "Question is too long (max 600 characters)."}), 400

    print(f"\n📩 User: {question}" + (f"  [model={model}]" if model else ""))
    try:
        answer = run_query(agent, question)
    except Exception as e:
        print(f"❌ Agent error: {e}")
        return jsonify({"error": f"Agent failed to process the question: {e}"}), 500

    print(f"🤖 Agent: {answer}\n")

    return jsonify({"answer": answer})


@app.route("/api/schema", methods=["GET"])
def schema():
    """Return the database tables for display in the UI."""
    tables = {
        "departments": ["id", "name", "budget"],
        "employees": ["id", "name", "department_id", "role", "salary", "hire_date"],
        "projects": ["id", "title", "dept_id", "status", "budget", "start_date", "end_date"],
        "project_assignments": ["employee_id", "project_id", "role"],
    }
    return jsonify(tables)


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")


if __name__ == "__main__":
    # Only open the browser on the actual run (not on Flask debug-reloader's child process)
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        Timer(1.0, open_browser).start()
    app.run(debug=True, port=5000)