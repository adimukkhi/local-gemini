from google import genai
from google.genai import types
from flask import Flask, request, render_template, redirect, url_for, session
from flask_session import Session
from dotenv import load_dotenv
import os
import markdown
import shutil

SESSION_FILE = "flask_session"
load_dotenv()
key = os.getenv("GEMINI_API_KEY")
app = Flask(__name__)
app.secret_key = "h"
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
Session(app)

client = genai.Client(api_key=key)

max_turns = 20

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []

    prompt = ""

    if request.method == "POST":
        prompt = request.form.get("name", "").strip()

    if prompt:
        history = session["chat_history"]
        history.append({"sender": "You", "text": prompt})

        recent_history = history[-max_turns:]

        api_history = []
        for msg in recent_history:
            role = "user" if msg["sender"] == "You" else "model"
            api_history.append(
                types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=msg["text"])]
                )
            )

        response = client.models.generate_content(
            model = "gemini-3.5-flash-lite",
            contents=api_history
        )

        history.append({"sender": "Gemini", "text": response.text})
        session["chat_history"] = history
        session.modified = True

    display_history = [
        {
            "sender": msg["sender"],
            "text": markdown.markdown(msg["text"]) if msg["sender"] == "Gemini" else msg["text"]
        }
        for msg in session.get("chat_history", [])
    ]

    return render_template("index.html", history=display_history)

@app.route("/clear", methods=["GET"])
def clear():
    session.pop("chat_history", None)
    return redirect(url_for("index"))

    

if __name__ == "__main__":
    shutil.rmtree(SESSION_FILE, ignore_errors=True)
    os.makedirs(SESSION_FILE, exist_ok=True)
    app.run(debug=True)