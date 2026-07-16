content = """<!DOCTYPE html>
<html>
<head>
  <title>Phetogo Projects - Login</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, sans-serif; background: #f0f4f8; display: flex; justify-content: center; align-items: center; height: 100vh; }
    .card { background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 360px; }
    h1 { color: #1a3c5e; font-size: 22px; margin-bottom: 6px; }
    p { color: #666; font-size: 13px; margin-bottom: 24px; }
    label { font-size: 13px; color: #333; font-weight: bold; display: block; margin-bottom: 6px; }
    input { width: 100%; padding: 10px; margin-bottom: 16px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; }
    button { width: 100%; padding: 10px; background: #1a3c5e; color: white; border: none; border-radius: 6px; font-size: 15px; cursor: pointer; }
    button:hover { background: #16324f; }
    .error { background: #f8d7da; color: #721c24; padding: 10px; border-radius: 6px; font-size: 13px; margin-bottom: 16px; }
    .credentials { background: #d4edda; color: #155724; padding: 10px; border-radius: 6px; font-size: 12px; margin-top: 16px; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Phetogo Projects</h1>
    <p>Task Management System - Please log in to continue</p>
    {% if error %}
    <div class="error">{{ error }}</div>
    {% endif %}
    <form method="POST">
      <label>Username</label>
      <input type="text" name="username" placeholder="Enter username" required />
      <label>Password</label>
      <input type="password" name="password" placeholder="Enter password" required />
      <button type="submit">Login</button>
    </form>
    <div class="credentials">
      <strong>Admin:</strong> username: admin | password: phetogo2026<br>
      <strong>Manager:</strong> username: manager | password: manager123
    </div>
  </div>
</body>
</html>"""

with open("templates/login.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")