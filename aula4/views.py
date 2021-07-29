from app import app


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/contato")
def contato():
    return "<form><input type='text'></input></form>"
