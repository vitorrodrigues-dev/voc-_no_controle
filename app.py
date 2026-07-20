from flask import Flask, render_template, request, redirect
from database import buscar_usuario, salvar_usuario, listar_alimentos, registrar_refeicao, progresso_do_dia, listar_refeicoes_do_dia, listar_dias_com_registro
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    return "Funcionando!"

@app.route("/ficha", methods=["GET", "POST"])
def ficha():
    if request.method == "POST":
        nome = request.form["nome"]
        idade = int(request.form["idade"])
        sexo = request.form["sexo"]
        peso_atual = float(request.form["peso_atual"])
        peso_desejado = float(request.form["peso_desejado"])
        altura = float(request.form["altura"])
        nivel_atividade = int(request.form["nivel_atividade"])
        objetivo = int(request.form["objetivo"])

        if sexo == "M":
            tmb = 88.36 + (13.4 * peso_atual) + (4.8 * altura) - (5.7 * idade)
        else:
            tmb = 447.6 + (9.2 * peso_atual) + (3.1 * altura) - (4.3 * idade)

        fatores = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725}
        tmb_total = tmb * fatores[nivel_atividade]

        if objetivo == 1:
            meta = tmb_total - 500
        elif objetivo == 2:
            meta = tmb_total + 400
        else:
            meta = tmb_total

        dados = {
            "nome": nome, "idade": idade, "sexo": sexo,
            "peso_atual": peso_atual, "peso_desejado": peso_desejado,
            "altura": altura, "nivel_atividade": nivel_atividade,
            "objetivo": objetivo, "tmb": tmb, "meta_calorica": meta
        }
        salvar_usuario(dados)
        return redirect("/ficha")

    usuario = buscar_usuario()
    return render_template("ficha.html", usuario=usuario)

@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    usuario = buscar_usuario()

    if request.method == "POST":
        alimento_id = int(request.form["alimento_id"])
        gramas = float(request.form["gramas"])
        nome_refeicao = request.form["nome_refeicao"]
        hoje = str(date.today())

        registrar_refeicao(usuario["id"], alimento_id, hoje, nome_refeicao, gramas)
        return redirect("/registrar")

    alimentos = listar_alimentos()
    return render_template("registrar.html", alimentos=alimentos)

@app.route("/progresso")
def progresso():
    usuario = buscar_usuario()
    hoje = str(date.today())

    totais = progresso_do_dia(usuario["id"], hoje)
    refeicoes = listar_refeicoes_do_dia(usuario["id"], hoje)

    return render_template("progresso.html", usuario=usuario, totais=totais, refeicoes=refeicoes, hoje=hoje)

@app.route("/historico")
def historico():
    usuario = buscar_usuario()
    dias = listar_dias_com_registro(usuario["id"])
    return render_template("historico.html", dias=dias)

@app.route("/historico/<data>")
def historico_dia(data):
    usuario = buscar_usuario()
    totais = progresso_do_dia(usuario["id"], data)
    refeicoes = listar_refeicoes_do_dia(usuario["id"], data)
    return render_template("progresso.html", usuario=usuario, totais=totais, refeicoes=refeicoes, hoje=data)

if __name__ == "__main__":
    app.run(debug=True)