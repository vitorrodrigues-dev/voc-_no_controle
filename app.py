from flask import Flask, request
from ficha import ficha_usuario
from dieta import menu_dieta

app = Flask(__name__)


# =========================
# MENU PRINCIPAL
# =========================
@app.route("/")
def menu():
    return """
    <h1>MENU PRINCIPAL</h1>

    <a href="/ficha"><button>Criar / Ver Ficha</button></a>
    <a href="/dieta"><button>Dietas</button></a>
    <br><br>
    """


# =========================
# FICHA (USA SUA LÓGICA)
# =========================
@app.route("/ficha", methods=["GET", "POST"])
def ficha():
    if request.method == "POST":
        # aqui sua lógica real da ficha roda (terminal adaptado)
        return ficha_usuario(web=True)

    return """
    <h1>FICHA DO USUÁRIO</h1>

    <form method="POST">
        <button type="submit">Criar / Ver Ficha</button>
    </form>

    <br>
    <a href="/">Voltar</a>
    """


# =========================
# DIETA MENU
# =========================
@app.route("/dieta")
def dieta():
    return """
    <h1>MENU DIETA</h1>

    <a href="/dieta/criar"><button>Criar Dieta</button></a>
    <a href="/dieta/refeicao"><button>Registrar Refeição</button></a>
    <a href="/dieta/progresso"><button>Ver Progresso</button></a>

    <br><br>
    <a href="/">Voltar</a>
    """


# =========================
# CRIAR DIETA (RODA SUA LÓGICA)
# =========================
@app.route("/dieta/criar", methods=["GET", "POST"])
def criar_dieta():
    if request.method == "POST":
        return menu_dieta(web="criar")

    return """
    <h1>CRIAR DIETA</h1>

    <form method="POST">
        <button type="submit">Iniciar criação da dieta</button>
    </form>

    <br>
    <a href="/dieta">Voltar</a>
    """


# =========================
# REGISTRAR REFEIÇÃO
# =========================
@app.route("/dieta/refeicao", methods=["GET", "POST"])
def refeicao():
    if request.method == "POST":
        return menu_dieta(web="refeicao")

    return """
    <h1>REGISTRAR REFEIÇÃO</h1>

    <form method="POST">
        <button type="submit">Iniciar registro</button>
    </form>

    <br>
    <a href="/dieta">Voltar</a>
    """


# =========================
# PROGRESSO
# =========================
@app.route("/dieta/progresso")
def progresso():
    return menu_dieta(web="progresso")


# =========================
# RODAR SERVIDOR
# =========================
if __name__ == "__main__":
    app.run(debug=True)