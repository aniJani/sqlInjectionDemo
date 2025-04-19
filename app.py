from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "your_secret_key_here"


# Initialize database
def init_db():
    if not os.path.exists("users.db"):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(
            """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """
        )
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("admin", "admin123"),
        )
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("user", "password123"),
        )
        conn.commit()
        conn.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login/insecure", methods=["GET", "POST"])
def insecure_login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()
        if user:
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid credentials"
    return render_template("insecure_login.html", error=error)


@app.route("/login/secure", methods=["GET", "POST"])
def secure_login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
        )
        user = cursor.fetchone()
        conn.close()
        if user:
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid credentials"
    return render_template("secure_login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("index"))
    return render_template("dashboard.html", username=session.get("username"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
