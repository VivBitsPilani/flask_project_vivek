#from flask import Flask, render_template_string, request

# Create Flask App
app = Flask(__name__)

# HTML Template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Web App</title>
</head>
<body>
    <h1>Welcome to the Simple Web App</h1>
    <form method="POST" action="/">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        <input type="submit" value="Submit">
    </form>
    {% if name %}
        <h2>Submitted Data:</h2>
        <p>Name: {{ name }}</p>
        <p>Email: {{ email }}</p>
    {% endif %}
</body>
</html>
"""

# Flask Routes
@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    email = None
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
    return render_template_string(html_template, name=name, email=email)

if __name__ == "__main__":
    app.run(debug=True)
