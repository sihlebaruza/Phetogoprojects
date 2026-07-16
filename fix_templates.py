files = {}

files['templates/dashboard.html'] = """<!DOCTYPE html>
<html>
<head>
  <title>Dashboard - Phetogo Projects</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, sans-serif; background: #f0f4f8; }
    nav { background: #1a3c5e; padding: 14px 30px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 8px rgba(0,0,0,0.2); }
    nav h1 { color: white; font-size: 18px; letter-spacing: 0.5px; }
    nav div a { color: #cce0f0; text-decoration: none; margin-left: 20px; font-size: 14px; padding: 6px 12px; border-radius: 4px; transition: background 0.2s; }
    nav div a:hover { background: rgba(255,255,255,0.15); color: white; }
    .container { max-width: 1100px; margin: 30px auto; padding: 0 24px; }
    .top-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
    .welcome { color: #1a3c5e; font-size: 20px; font-weight: bold; }
    .welcome span { color: #555; font-weight: normal; font-size: 14px; margin-left: 10px; }
    .btn { display: inline-block; padding: 10px 20px; background: #1a3c5e; color: white; border-radius: 6px; text-decoration: none; font-size: 14px; transition: background 0.2s; }
    .btn:hover { background: #16324f; }
    .filters { background: white; padding: 16px 20px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 20px; display: flex; gap: 12px; align-items: center; flex-wrap: wrap; }
    .filters input { padding: 8px 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; width: 250px; }
    .filters select { padding: 8px 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; }
    .filters button { padding: 8px 16px; background: #1a3c5e; color: white; border: none; border-radius: 6px; font-size: 14px; cursor: pointer; }
    .filters button:hover { background: #16324f; }
    .filters a { padding: 8px 16px; background: #eee; color: #333; border-radius: 6px; font-size: 14px; text-decoration: none; }
    .filters a:hover { background: #ddd; }
    .stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }
    .stat-card { background: white; border-radius: 10px; padding: 18px 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 4px solid #1a3c5e; }
    .stat-card .num { font-size: 28px; font-weight: bold; color: #1a3c5e; }
    .stat-card .lbl { font-size: 12px; color: #888; margin-top: 4px; }
    .stat-card.completed { border-left-color: #28a745; }
    .stat-card.completed .num { color: #28a745; }
    .stat-card.progress { border-left-color: #007bff; }
    .stat-card.progress .num { color: #007bff; }
    .stat-card.pending { border-left-color: #ffc107; }
    .stat-card.pending .num { color: #e6ac00; }
    table { width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
    th { background: #1a3c5e; color: white; padding: 13px 16px; text-align: left; font-size: 13px; font-weight: 600; }
    td { padding: 12px 16px; border-bottom: 1px solid #f0f0f0; font-size: 13px; color: #333; }
    tr:last-child td { border-bottom: none; }
    tr:hover td { background: #f8fbff; }
    .badge { padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: bold; }
    .Pending { background: #fff3cd; color: #856404; }
    .In-Progress { background: #cce5ff; color: #004085; }
    .Completed { background: #d4edda; color: #155724; }
    .actions { display: flex; gap: 8px; }
    .btn-edit { padding: 4px 10px; background: #17a2b8; color: white; border-radius: 4px; text-decoration: none; font-size: 12px; }
    .btn-edit:hover { background: #138496; }
    .btn-update { padding: 4px 10px; background: #ffc107; color: #333; border-radius: 4px; text-decoration: none; font-size: 12px; }
    .btn-update:hover { background: #e0a800; }
    .btn-delete { padding: 4px 10px; background: #dc3545; color: white; border-radius: 4px; text-decoration: none; font-size: 12px; }
    .btn-delete:hover { background: #c82333; }
    .empty { text-align: center; padding: 40px; color: #999; }
    .footer { text-align: center; color: #aaa; font-size: 12px; margin-top: 30px; padding-bottom: 20px; }
  </style>
</head>
<body>
  <nav>
    <h1>&#128203; Phetogo Projects — Task Manager</h1>
    <div>
      <a href="/dashboard">Dashboard</a>
      <a href="/add">Add Task</a>
      <a href="/reports">Reports</a>
      <a href="/logout">Logout</a>
    </div>
  </nav>
  <div class="container">
    <div class="top-bar">
      <div class="welcome">Dashboard <span>Logged in as: {{ user }}</span></div>
      <a href="/add" class="btn">+ Add New Task</a>
    </div>

    <div class="stats">
      <div class="stat-card">
        <div class="num">{{ tasks|length }}</div>
        <div class="lbl">Showing Tasks</div>
      </div>
      <div class="stat-card completed">
        <div class="num">{{ tasks|selectattr('4', 'equalto', 'Completed')|list|length }}</div>
        <div class="lbl">Completed</div>
      </div>
      <div class="stat-card progress">
        <div class="num">{{ tasks|selectattr('4', 'equalto', 'In Progress')|list|length }}</div>
        <div class="lbl">In Progress</div>
      </div>
      <div class="stat-card pending">
        <div class="num">{{ tasks|selectattr('4', 'equalto', 'Pending')|list|length }}</div>
        <div class="lbl">Pending</div>
      </div>
    </div>

    <form class="filters" method="GET" action="/dashboard">
      <input type="text" name="search" placeholder="Search client or task..." value="{{ search }}" />
      <select name="status">
        <option value="All" {% if status_filter == 'All' %}selected{% endif %}>All Statuses</option>
        <option value="Pending" {% if status_filter == 'Pending' %}selected{% endif %}>Pending</option>
        <option value="In Progress" {% if status_filter == 'In Progress' %}selected{% endif %}>In Progress</option>
        <option value="Completed" {% if status_filter == 'Completed' %}selected{% endif %}>Completed</option>
      </select>
      <button type="submit">Search</button>
      <a href="/dashboard">Clear</a>
    </form>

    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>Client</th>
          <th>Description</th>
          <th>Assigned To</th>
          <th>Status</th>
          <th>Date</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {% if tasks %}
          {% for task in tasks %}
          <tr>
            <td>{{ task[0] }}</td>
            <td><strong>{{ task[1] }}</strong></td>
            <td>{{ task[2] }}</td>
            <td>{{ task[3] }}</td>
            <td><span class="badge {{ task[4].replace(' ', '-') }}">{{ task[4] }}</span></td>
            <td>{{ task[5] }}</td>
            <td>
              <div class="actions">
                <a href="/edit/{{ task[0] }}" class="btn-edit">Edit</a>
                <a href="/update/{{ task[0] }}" class="btn-update">Status</a>
                <a href="/delete/{{ task[0] }}" class="btn-delete" onclick="return confirm('Delete this task?')">Delete</a>
              </div>
            </td>
          </tr>
          {% endfor %}
        {% else %}
          <tr><td colspan="7" class="empty">No tasks found. Click Add New Task to get started.</td></tr>
        {% endif %}
      </tbody>
    </table>
    <div class="footer">Phetogo Projects Task Management System &copy; 2026</div>
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
    nav { background: #1a3c5e; padding: 14px 30px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 8px rgba(0,0,0,0.2); }
    nav h1 { color: white; font-size: 18px; }
    nav div a { color: #cce0f0; text-decoration: none; margin-left: 20px; font-size: 14px; padding: 6px 12px; border-radius: 4px; transition: background 0.2s; }
    nav div a:hover { background: rgba(255,255,255,0.15); color: white; }
    .container { max-width: 600px; margin: 40px auto; padding: 0 24px; }
    .back { display: inline-block; margin-bottom: 16px; color: #1a3c5e; text-decoration: none; font-size: 13px; }
    .back:hover { text-decoration: underline; }
    .card { background: white; padding: 32px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
    .card-header { border-bottom: 2px solid #f0f0f0; padding-bottom: 16px; margin-bottom: 24px; }
    h2 { color: #1a3c5e; font-size: 20px; }
    h2 span { font-size: 13px; color: #888; font-weight: normal; margin-left: 8px; }
    label { font-size: 13px; font-weight: bold; color: #444; display: block; margin-bottom: 6px; }
    input, textarea { width: 100%; padding: 10px 12px; border: 1px solid #ddd; border-radius: 6px; font-size: 14px; margin-bottom: 20px; transition: border 0.2s; }
    input:focus, textarea:focus { border-color: #1a3c5e; outline: none; }
    textarea { height: 110px; resize: vertical; }
    .btn-row { display: flex; gap: 10px; }
    button { padding: 10px 24px; background: #1a3c5e; color: white; border: none; border-radius: 6px; font-size: 14px; cursor: pointer; transition: background 0.2s; }
    button:hover { background: #16324f; }
    .btn-cancel { padding: 10px 24px; background: #eee; color: #333; border-radius: 6px; font-size: 14px; text-decoration: none; }
    .btn-cancel:hover { background: #ddd; }
  </style>
</head>
<body>
  <nav>
    <h1>&#128203; Phetogo Projects — Task Manager</h1>
    <div>
      <a href="/dashboard">Dashboard</a>
      <a href="/add">Add Task</a>
      <a href="/reports">Reports</a>
      <a href="/logout">Logout</a>
    </div>
  </nav>
  <div class="container">
    <a href="/dashboard" class="back">&#8592; Back to Dashboard</a>
    <div class="card">
      <div class="card-header">
        <h2>Log New Client Task <span>Logged in as: {{ user }}</span></h2>
      </div>
      <form method="POST">
        <label>Client Name</label>
        <input type="text" name="client" placeholder="e.g. ABC Company" required />
        <label>Task Description</label>
        <textarea name="description" placeholder="Describe the task or request in detail..." required></textarea>
        <div class="btn-row">
          <button type="submit">Add Task</button>
          <a href="/dashboard" class="btn-cancel">Cancel</a>
        </div>
      </form>
    </div>
  </div>
</body>
</html>"""

files['templates/edit_task.html'] = """<!DOCTYPE html>
<html>
<head>
  <title>Edit Task - Phetogo Projects</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, sans-serif; background: #f0f4f8; }
    nav { background: #1a3c5e; padding: 14px 30px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 8px rgba(0,0,0,0.2); }
    nav h1 { color: white; font-size: 18px; }
    nav div a { color: #cce0f0; text-decoration: none; margin-left: 20px; font-size: 14px; padding: 6px 12px; border-radius: 4px; transition: background 0.2s; }
    nav div a:hover { background: rgba(255,255,255,0.15); color: white; }
    .container { max-width: 600px; margin: 40px auto; padding: 0 24px; }
    .back { display: inline-block; margin-bottom: 16px; color: #1a3c5e; text-decoration: none; font-size: 13px; }
    .back:hover { text-decoration: underline; }
    .card { background: white; padding: 32px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
    .card-header { border-bottom: 2px solid #f0f0f0; padding-bottom: 16px; margin-bottom: 24px; }
    h2 { color: #1a3c5e; font-size: 20px; }
    label { font-size: 13px; font-weight: bold; color: #444; display: block; margin-bottom: 6px; }
    input, textarea, select { width: 100%; padding: 10px 12px; border: 1px solid #ddd; border-radius: 6px; font-size: 14px; margin-bottom: 20px; transition: border 0.2s; }
    input:focus, textarea:focus, select:focus { border-color: #1a3c5e; outline: none; }
    textarea { height: 110px; resize: vertical; }
    .btn-row { display: flex; gap: 10px; }
    button { padding: 10px 24px; background: #17a2b8; color: white; border: none; border-radius: 6px; font-size: 14px; cursor: pointer; }
    button:hover { background: #138496; }
    .btn-cancel { padding: 10px 24px; background: #eee; color: #333; border-radius: 6px; font-size: 14px; text-decoration: none; }
    .btn-cancel:hover { background: #ddd; }
  </style>
</head>
<body>
  <nav>
    <h1>&#128203; Phetogo Projects — Task Manager</h1>
    <div>
      <a href="/dashboard">Dashboard</a>
      <a href="/add">Add Task</a>
      <a href="/reports">Reports</a>
      <a href="/logout">Logout</a>
    </div>
  </nav>
  <div class="container">
    <a href="/dashboard" class="back">&#8592; Back to Dashboard</a>
    <div class="card">
      <div class="card-header">
        <h2>Edit Task #{{ task[0] }}</h2>
      </div>
      <form method="POST">
        <label>Client Name</label>
        <input type="text" name="client" value="{{ task[1] }}" required />
        <label>Task Description</label>
        <textarea name="description" required>{{ task[2] }}</textarea>
        <label>Assigned To</label>
        <input type="text" name="assigned_to" value="{{ task[3] }}" required />
        <label>Status</label>
        <select name="status">
          <option value="Pending" {% if task[4] == 'Pending' %}selected{% endif %}>Pending</option>
          <option value="In Progress" {% if task[4] == 'In Progress' %}selected{% endif %}>In Progress</option>
          <option value="Completed" {% if task[4] == 'Completed' %}selected{% endif %}>Completed</option>
        </select>
        <div class="btn-row">
          <button type="submit">Save Changes</button>
          <a href="/dashboard" class="btn-cancel">Cancel</a>
        </div>
      </form>
    </div>
  </div>
</body>
</html>"""

files['templates/update_task.html'] = """<!DOCTYPE html>
<html>
<head>
  <title>Update Status - Phetogo Projects</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, sans-serif; background: #f0f4f8; }
    nav { background: #1a3c5e; padding: 14px 30px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 8px rgba(0,0,0,0.2); }
    nav h1 { color: white; font-size: 18px; }
    nav div a { color: #cce0f0; text-decoration: none; margin-left: 20px; font-size: 14px; padding: 6px 12px; border-radius: 4px; }
    nav div a:hover { background: rgba(255,255,255,0.15); color: white; }
    .container { max-width: 500px; margin: 40px auto; padding: 0 24px; }
    .back { display: inline-block; margin-bottom: 16px; color: #1a3c5e; text-decoration: none; font-size: 13px; }
    .card { background: white; padding: 32px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
    .card-header { border-bottom: 2px solid #f0f0f0; padding-bottom: 16px; margin-bottom: 24px; }
    h2 { color: #1a3c5e; font-size: 20px; }
    label { font-size: 13px; font-weight: bold; color: #444; display: block; margin-bottom: 6px; }
    select { width: 100%; padding: 10px 12px; border: 1px solid #ddd; border-radius: 6px; font-size: 14px; margin-bottom: 20px; }
    select:focus { border-color: #1a3c5e; outline: none; }
    .btn-row { display: flex; gap: 10px; }
    button { padding: 10px 24px; background: #ffc107; color: #333; border: none; border-radius: 6px; font-size: 14px; cursor: pointer; font-weight: bold; }
    button:hover { background: #e0a800; }
    .btn-cancel { padding: 10px 24px; background: #eee; color: #333; border-radius: 6px; font-size: 14px; text-decoration: none; }
    .btn-cancel:hover { background: #ddd; }
  </style>
</head>
<body>
  <nav>
    <h1>&#128203; Phetogo Projects — Task Manager</h1>
    <div>
      <a href="/dashboard">Dashboard</a>
      <a href="/add">Add Task</a>
      <a href="/reports">Reports</a>
      <a href="/logout">Logout</a>
    </div>
  </nav>
  <div class="container">
    <a href="/dashboard" class="back">&#8592; Back to Dashboard</a>
    <div class="card">
      <div class="card-header">
        <h2>Update Task #{{ task_id }} Status</h2>
      </div>
      <form method="POST">
        <label>Select New Status</label>
        <select name="status">
          <option value="Pending">Pending</option>
          <option value="In Progress">In Progress</option>
          <option value="Completed">Completed</option>
        </select>
        <div class="btn-row">
          <button type="submit">Save Update</button>
          <a href="/dashboard" class="btn-cancel">Cancel</a>
        </div>
      </form>
    </div>
  </div>
</body>
</html>"""

files['templates/reports.html'] = """<!DOCTYPE html>
<html>
<head>
  <title>Reports - Phetogo Projects</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, sans-serif; background: #f0f4f8; }
    nav { background: #1a3c5e; padding: 14px 30px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 8px rgba(0,0,0,0.2); }
    nav h1 { color: white; font-size: 18px; }
    nav div a { color: #cce0f0; text-decoration: none; margin-left: 20px; font-size: 14px; padding: 6px 12px; border-radius: 4px; }
    nav div a:hover { background: rgba(255,255,255,0.15); color: white; }
    .container { max-width: 900px; margin: 40px auto; padding: 0 24px; }
    .back { display: inline-block; margin-bottom: 16px; color: #1a3c5e; text-decoration: none; font-size: 13px; }
    .page-header { margin-bottom: 24px; }
    h2 { color: #1a3c5e; font-size: 22px; margin-bottom: 4px; }
    .date { color: #888; font-size: 13px; }
    .cards { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 30px; }
    .stat { background: white; border-radius: 10px; padding: 24px 20px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-top: 4px solid #1a3c5e; }
    .stat .number { font-size: 42px; font-weight: bold; }
    .stat .label { font-size: 13px; color: #666; margin-top: 6px; }
    .total .number { color: #1a3c5e; }
    .total { border-top-color: #1a3c5e; }
    .completed .number { color: #28a745; }
    .completed { border-top-color: #28a745; }
    .progress .number { color: #007bff; }
    .progress { border-top-color: #007bff; }
    .pending .number { color: #e6ac00; }
    .pending { border-top-color: #ffc107; }
    .progress-section { background: white; border-radius: 10px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
    .progress-section h3 { color: #1a3c5e; margin-bottom: 16px; font-size: 16px; }
    .bar-wrap { margin-bottom: 14px; }
    .bar-label { display: flex; justify-content: space-between; font-size: 13px; color: #555; margin-bottom: 6px; }
    .bar-bg { background: #eee; border-radius: 20px; height: 12px; overflow: hidden; }
    .bar-fill { height: 100%; border-radius: 20px; transition: width 0.5s; }
    .bar-completed { background: #28a745; }
    .bar-progress { background: #007bff; }
    .bar-pending { background: #ffc107; }
    .footer { text-align: center; color: #aaa; font-size: 12px; margin-top: 30px; padding-bottom: 20px; }
  </style>
</head>
<body>
  <nav>
    <h1>&#128203; Phetogo Projects — Task Manager</h1>
    <div>
      <a href="/dashboard">Dashboard</a>
      <a href="/add">Add Task</a>
      <a href="/reports">Reports</a>
      <a href="/logout">Logout</a>
    </div>
  </nav>
  <div class="container">
    <a href="/dashboard" class="back">&#8592; Back to Dashboard</a>
    <div class="page-header">
      <h2>Daily Task Report</h2>
      <p class="date">Date: {{ data.date }} &nbsp;|&nbsp; Logged in as: {{ user }}</p>
    </div>
    <div class="cards">
      <div class="stat total">
        <div class="number">{{ data.total }}</div>
        <div class="label">Total Tasks Today</div>
      </div>
      <div class="stat completed">
        <div class="number">{{ data.completed }}</div>
        <div class="label">Completed</div>
      </div>
      <div class="stat progress">
        <div class="number">{{ data.in_progress }}</div>
        <div class="label">In Progress</div>
      </div>
      <div class="stat pending">
        <div class="number">{{ data.pending }}</div>
        <div class="label">Pending</div>
      </div>
    </div>
    <div class="progress-section">
      <h3>Task Completion Breakdown</h3>
      {% if data.total > 0 %}
      <div class="bar-wrap">
        <div class="bar-label"><span>Completed</span><span>{{ data.completed }} / {{ data.total }}</span></div>
        <div class="bar-bg"><div class="bar-fill bar-completed" style="width: {{ (data.completed / data.total * 100)|int }}%"></div></div>
      </div>
      <div class="bar-wrap">
        <div class="bar-label"><span>In Progress</span><span>{{ data.in_progress }} / {{ data.total }}</span></div>
        <div class="bar-bg"><div class="bar-fill bar-progress" style="width: {{ (data.in_progress / data.total * 100)|int }}%"></div></div>
      </div>
      <div class="bar-wrap">
        <div class="bar-label"><span>Pending</span><span>{{ data.pending }} / {{ data.total }}</span></div>
        <div class="bar-bg"><div class="bar-fill bar-pending" style="width: {{ (data.pending / data.total * 100)|int }}%"></div></div>
      </div>
      {% else %}
      <p style="color:#999; font-size:13px;">No tasks logged today yet.</p>
      {% endif %}
    </div>
    <div class="footer">Phetogo Projects Task Management System &copy; 2026</div>
  </div>
</body>
</html>"""

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed: {path}")

print("All files done!")