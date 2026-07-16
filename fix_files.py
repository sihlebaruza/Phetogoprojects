import os

files = {}

files['templates/login.html'] = """<!DOCTYPE html>
<html>
<head>
  <title>Phetogo Projects - Login</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, sans-serif; background: #f0f4f8; display: flex; justify-content: center; align-items: center; height: 100vh; }
    .card { background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 360px; }
    h1 { color: #1a3c5e; font-size: 22px; margin-bottom: 6px; }
    p { color: #666; font-size: 13px; margin-bottom: 24px; }
    label { font-size: 13px; color: #333; font-weight: bold; }
    input { width: 100%; padding: 10px; margin: 8px 0 20px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; }
    button { width: 100%; padding: 10px; background: #1a3c5e; color: white; border: none; border-radius: 6px; font-size: 15px; cursor: pointer; }
    button:hover { background: #16324f; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Phetogo Projects</h1>
    <p>Task Management System - Please log in to continue</p>
    <form method="POST">
      <label>Your Name</label>
      <input type="text" name="username" placeholder="Enter your name" required />
      <button type="submit">Login</button>
    </form>
  </div>
</body>
</html>"""

files['templates/dashboard.html'] = """<!DOCTYPE html>
<html>
<head>
  <title>Dashboard - Phetogo Projects</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, sans-serif; background: #f0f4f8; }
    nav { background: #1a3c5e; padding: 14px 30px; display: flex; justify-content: space-between; align-items: center; }
    nav h1 { color: white; font-size: 18px; }
    nav div a { color: #cce0f0; text-decoration: none; margin-left: 20px; font-size: 14px; }
    nav div a:hover { color: white; }
    .container { max-width: 1000px; margin: 30px auto; padding: 0 20px; }
    .welcome { color: #1a3c5e; font-size: 20px; margin-bottom: 20px; }
    .btn { display: inline-block; padding: 10px 20px; background: #1a3c5e; color: white; border-radius: 6px; text-decoration: none; font-size: 14px; margin-bottom: 20px; }
    .btn:hover { background: #16324f; }
    table { width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
    th { background: #1a3c5e; color: white; padding: 12px 16px; text-align: left; font-size: 13px; }
    td { padding: 12px 16px; border-bottom: 1px solid #eee; font-size: 13px; color: #333; }
    tr:last-child td { border-bottom: none; }
    .badge { padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: bold; }
    .Pending { background: #fff3cd; color: #856404; }
    .In-Progress { background: #cce5ff; color: #004085; }
    .Completed { background: #d4edda; color: #155724; }
    .action { color: #1a3c5e; text-decoration: none; font-weight: bold; }
    .empty { text-align: center; padding: 40px; color: #999; }
  </style>
</head>
<body>
  <nav>
    <h1>Phetogo Projects - Task Manager</h1>
    <div>
      <a href="/dashboard">Dashboard</a>
      <a href="/add">Add Task</a>
      <a href="/reports">Reports</a>
      <a href="/logout">Logout</a>
    </div>
  </nav>
  <div class="container">
    <p class="welcome">Welcome, {{ user }}</p>
    <a href="/add" class="btn">+ Add New Task</a>
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>Client</th>
          <th>Description</th>
          <th>Assigned To</th>
          <th>Status</th>
          <th>Date</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {% if tasks %}
          {% for task in tasks %}
          <tr>
            <td>{{ task[0] }}</td>
            <td>{{ task[1] }}</td>
            <td>{{ task[2] }}</td>
            <td>{{ task[3] }}</td>
            <td><span class="badge {{ task[4].replace(' ', '-') }}">{{ task[4] }}</span></td>
            <td>{{ task[5] }}</td>
            <td><a href="/update/{{ task[0] }}" class="action">Update</a></td>
          </tr>
          {% endfor %}
        {% else %}
          <tr><td colspan="7" class="empty">No tasks yet. Click Add New Task to get started.</td></tr>
        {% endif %}
      </tbody>
    </table>
  </div>
</body>
</html>"""

files['templates/add_task.html'] = """<!DOCTYPE html>
<html>
<head>
  <title>Add Task - Phetogo Projects</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, sans-serif; background: #f0f4f8; }
    nav { background: #1a3c5e; padding: 14px 30px; display: flex; justify-content: space-between; align-items: center; }
    nav h1 { color: white; font-size: 18px; }
    nav div a { color: #cce0f0; text-decoration: none; margin-left: 20px; font-size: 14px; }
    nav div a:hover { color: white; }
    .container { max-width: 600px; margin: 40px auto; padding: 0 20px; }
    .card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
    h2 { color: #1a3c5e; margin-bottom: 20px; font-size: 18px; }
    label { font-size: 13px; font-weight: bold; color: #333; display: block; margin-bottom: 6px; }
    input, textarea { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; margin-bottom: 18px; }
    textarea { height: 100px; resize: vertical; }
    button { padding: 10px 24px; background: #1a3c5e; color: white; border: none; border-radius: 6px; font-size: 14px; cursor: pointer; }
    button:hover { background: #16324f; }
    .back { display: inline-block; margin-bottom: 16px; color: #1a3c5e; text-decoration: none; font-size: 13px; }
  </style>
</head>
<body>
  <nav>
    <h1>Phetogo Projects - Task Manager</h1>
    <div>
      <a href="/dashboard">Dashboard</a>
      <a href="/add">Add Task</a>
      <a href="/reports">Reports</a>
      <a href="/logout">Logout</a>
    </div>
  </nav>
  <div class="container">
    <a href="/dashboard" class="back">Back to Dashboard</a>
    <div class="card">
      <h2>Log New Client Task</h2>
      <form method="POST">
        <label>Client Name</label>
        <input type="text" name="client" placeholder="e.g. ABC Company" required />
        <label>Task Description</label>
        <textarea name="description" placeholder="Describe the task or request..." required></textarea>
        <button type="submit">Add Task</button>
      </form>
    </div>
  </div>
</body>
</html>"""

files['templates/update_task.html'] = """<!DOCTYPE html>
<html>
<head>
  <title>Update Task - Phetogo Projects</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, sans-serif; background: #f0f4f8; }
    nav { background: #1a3c5e; padding: 14px 30px; display: flex; justify-content: space-between; align-items: center; }
    nav h1 { color: white; font-size: 18px; }
    nav div a { color: #cce0f0; text-decoration: none; margin-left: 20px; font-size: 14px; }
    nav div a:hover { color: white; }
    .container { max-width: 600px; margin: 40px auto; padding: 0 20px; }
    .card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
    h2 { color: #1a3c5e; margin-bottom: 20px; font-size: 18px; }
    label { font-size: 13px; font-weight: bold; color: #333; display: block; margin-bottom: 6px; }
    select { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; margin-bottom: 18px; }
    button { padding: 10px 24px; background: #1a3c5e; color: white; border: none; border-radius: 6px; font-size: 14px; cursor: pointer; }
    button:hover { background: #16324f; }
    .back { display: inline-block; margin-bottom: 16px; color: #1a3c5e; text-decoration: none; font-size: 13px; }
  </style>
</head>
<body>
  <nav>
    <h1>Phetogo Projects - Task Manager</h1>
    <div>
      <a href="/dashboard">Dashboard</a>
      <a href="/add">Add Task</a>
      <a href="/reports">Reports</a>
      <a href="/logout">Logout</a>
    </div>
  </nav>
  <div class="container">
    <a href="/dashboard" class="back">Back to Dashboard</a>
    <div class="card">