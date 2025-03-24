from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>HTTP</title>
</head>
<body>
    <h2>Welcome to the Challenge!</h2>
    <form action="/flag" method="POST">
        <button type="submit">FLAG</button>
    </form>
</body>
</html>
"""

@app.route("/")
def home():
    return PAGE

@app.route("/flag", methods=["POST", "GET"])
def flag():
    if request.method == "GET":
        return "Congratulations! You GET the flag: HTTP_GET_the_flAg"
    return "You want to get the flag? HeHe"


def handler(request, *args, **kwargs):
    return app.wsgi_app(request.environ, lambda status, headers: None)
