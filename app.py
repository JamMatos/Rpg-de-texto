'''Arquivo que roda o jogo no modo web'''
from flask import Flask, request, render_template, session
from models.jogador import Jogador

app = Flask(__name__)
app.secret_key = "segredo123"

@app.route("/")
def index():
    '''Método para chamar o caminho principal'''
    return render_template('index.html')

@app.route("/resposta", methods=["GET", "POST"])
def resposta():
    '''Função que capturar o nome do jogador'''
    prota = Jogador()
    prota.nome = request.form.get("nome")
    session["nome_jogador"] = prota.nome

    return "Ok"

if __name__ == "__main__":
    app.run(debug=True)
