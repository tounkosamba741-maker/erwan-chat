
from flask import Flask, request, redirect, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

messages = []

PAGE = """
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ERWAN CHAT</title>
<style>
body {
    margin: 0;
    background: #101827;
    color: white;
    font-family: Arial, sans-serif;
}
header {
    background: #075e54;
    padding: 22px;
    text-align: center;
    font-size: 25px;
    font-weight: bold;
}
main {
    max-width: 600px;
    margin: 25px auto;
    padding: 15px;
}
.messages {
    background: #1e293b;
    border-radius: 12px;
    padding: 15px;
    min-height: 250px;
}
.message {
    background: #075e54;
    padding: 12px;
    margin: 10px 0;
    border-radius: 10px;
    overflow-wrap: anywhere;
}
form {
    margin-top: 20px;
}
input {
    box-sizing: border-box;
    width: 100%;
    padding: 15px;
    margin: 7px 0;
    border: none;
    border-radius: 8px;
}
button {
    width: 100%;
    padding: 15px;
    background: #00a884;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 17px;
}
</style>
</head>
<body>
<header>💬 ERWAN CHAT</header>
<main>
<h2>Bienvenue sur ERWAN CHAT</h2>
<div class="messages">
{% for m in messages %}
<div class="message">
<strong>{{ m.name }}</strong><br>
{{ m.text }}<br>
<small>{{ m.time }}</small>
</div>
{% else %}
<p>Aucun message pour le moment.</p>
{% endfor %}
</div>
<form method="POST">
<input name="name" placeholder="Ton nom" required>
<input name="message" placeholder="Écris ton message..." required>
<button type="submit">Envoyer 💬</button>
</form>
</main>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip()[:30]
        text = request.form.get("message", "").strip()[:500]

        if name and text:
            messages.append({
                "name": name,
                "text": text,
                "time": datetime.now().strftime("%H:%M")
            })

        return redirect("/")

    return render_template_string(PAGE, messages=messages)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
)
  
