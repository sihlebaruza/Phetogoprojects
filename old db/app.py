from flask import Flask, render_template, request, redirect, session, url_for, flash
from database import init_db, get_tasks, add_task, update_task_status, get_report

app = Flask(__name__)
app.secret_key = "phetogo2026secretkey123"

init_db()

USERS = {
    "admin": "admin",
    "Sihle": "phetogo2026",
    "Kamo": "phetogo2026",
    "manager": "manager123"
}

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in USERS and USERS[username] == password:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password. Please try again."
    return render_template("login.html", error=error)

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