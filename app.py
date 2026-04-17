from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def menu_principal():
    return """
    <h1>Menu Principal</h1>
    <p>Escolha uma opção:</p>
    <ul>
        <li><a href="/dieta">1. Ver Dieta</a></li>
        <li><a href="/ficha">2. Ver Ficha</a></li>
    </ul>
    """

@app.route('/dieta')
def dieta():
    # Aqui você chama a lógica do seu arquivo dieta.py
    return "Aqui aparece a dieta (Puxado do seu código antigo)"

@app.route('/ficha')
def ficha():
    # Aqui você chama a lógica do seu arquivo ficha.py
    return "Aqui aparece a ficha"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)