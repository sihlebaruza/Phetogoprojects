from flask import Flask, render_template, request, redirect, session, url_for
from database import init_db, get_tasks, add_task, update_task_status, get_report
import os

app = Flask(__name__)
app.secret_key = "phetogo2026secretkey123"
app.config['SESSION_TYPE'] = 'filesystem'

init_db()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["username"]
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    tasks = get_tasks()
    return render_template("dashboard.html", tasks=tasks, user=session["user"])

@app.route("/add", methods=["GET", "POST"])
def add():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        client = request.form["client"]
        description = request.form["description"]
        add_task(client, description, session["user"])
        return redirect(url_for("dashboard"))
    return render_template("add_task.html", user=session["user"])

@app.route("/update/<int:task_id>", methods=["GET", "POST"])
def update(task_id):
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        status = request.form["status"]
        update_task_status(task_id, status)
        return redirect(url_for("dashboard"))
    return render_template("update_task.html", task_id=task_id, user=session["user"])

@app.route("/reports")
def reports():
    if "user" not in session:
        return redirect(url_for("login"))
    data = get_report()
    return render_template("reports.html", data=data, user=session["user"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)