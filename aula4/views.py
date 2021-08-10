"""Extensão do Flask - Uma coisa que é chamada."""


def init_app(app):
    """Factory de inicialização de extensões"""

    @app.route("/")
    def index():
        return "<h1>Hello World</h1>"

    @app.route("/contato")
    def contato():
        return "<form><input type='text'></input></form>"
