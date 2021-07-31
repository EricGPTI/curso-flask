# Contextos 
from flask import flask
app = Flask(__NAME__)

## 1 - Configuração - Deve acontecer antes da execução do programa.
### Add configuração
app.config["algum_valor"] = "outro_Valor"
app.config["SQLALCHEMY_DB_URI"] = "mysql://.."

### Registrar Rotas
@app.route("/path")
def minha_function():
    pass
#### ou
app.add_url_rule("/path", callable)

###Inicializar Extensões
from flas_admin import Admin
admin.init_app(app)

### Registrar Blueprints
app.register_blueprints(...)
app.error_handle(...)

### add hooks
@app.before_request(...)

## 2 - App Context
### APP está pronta! `app`. A aplicação entra neste estado quando rodamos o flask run.
### Testar
#### app.test_client
#### debug
#### objetos globais do Flask
#### (request, session, g)
#### Hooks
#### Até aqui nenhuma requisição foi feita.

## 3 - Request Context
### Aqui é onde a maior parte das regras de negócio acontecem
#### from flask import request, session
#### request.args
#### request.form