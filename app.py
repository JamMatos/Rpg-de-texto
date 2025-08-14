"""Arquivo que roda o jogo no modo web"""

from flask import Flask, request, render_template, session, redirect, url_for
from models.jogador import Jogador
from models.monstros import Zombie
from routers.combate.interface_web import aplicar_acao

app = Flask(__name__)
app.secret_key = "segredo123"


@app.route("/")
def index():
    """Método para chamar o caminho principal"""
    return render_template("registro.html")

@app.route("/jogo", methods=["GET", "POST"])
def jogo():
    """Função que capturar o nome do jogador"""
    prota = Jogador()
    prota.nome = request.form.get("nome")
    session["prota"] = {
        "nome": prota.nome,
        "vida": prota.vida,
        "dano": prota.dano,
        "energia": prota.energia,
        "defesa": prota.defesa,
        "inventario": prota.inventario,
        "dano_min": prota.dano_min,
        "dano_max": prota.dano_max,
    }

    return render_template("jogo.html", nome=prota.nome)


@app.route("/nivel_primeiro", methods=["GET", "POST"])
def combate():
    '''Método que executa o combate'''
    prota = session["prota"]
    zombie = Zombie()
    session["zombie"] = {
        "nome": zombie.nome,
        "dano": zombie.dano,
        "vida": zombie.vida,
        "dano_min": zombie.dano_min,
        "dano_max": zombie.dano_max
    }
    zombie = session["zombie"]
    #zombie = session.get("zombie") or {
    #     "nome": "Zombie",
    #     "vida": 50,
    #     "dano_min": 5,
    #     "dano_max": 10,
    # }
    inimigos = [zombie]
    animal = prota.get("animal") if "animal" in prota else None

    tem_magia = any(
        item["tipo"] == "Magico" and item["ativo"] for item in prota["inventario"]
    )
    tem_pocao = any(
        item["tipo"] == "Pocao" and item["quantidade"] > 0
        for item in prota["inventario"]
    )
    tem_pato = bool(animal)

    if request.method == "POST":
        acao = request.form.get("acao")

        # Se for magia ou poção, redireciona para tela de escolha
        if acao == "2" and tem_magia:
            magias = [
                i for i in prota["inventario"] if i["tipo"] == "Magico" and i["ativo"]
            ]
            return render_template(
                "escolher_item.html", tipo="magia", acao=acao, itens=magias
            )

        if acao == "3" and tem_pocao:
            pocoes = [
                i
                for i in prota["inventario"]
                if i["tipo"] == "Pocao" and i["quantidade"] > 0
            ]
            return render_template(
                "escolher_item.html", tipo="pocao", acao=acao, itens=pocoes
            )

        # Se não precisar escolher item
        prota, inimigos = aplicar_acao(acao, prota, inimigos, animal=animal)
        session["prota"] = prota
        session["zombie"] = inimigos[0]
        return redirect(url_for("combate"))

    return render_template(
        "combate.html",
        nivel=1,
        prota=prota,
        inimigo=zombie,
        tem_magia=tem_magia,
        tem_pocao=tem_pocao,
        tem_pato=tem_pato,
    )


@app.route("/usar_item", methods=["POST"])
def usar_item():
    '''Método para utilizar dos itens'''
    acao = request.form.get("acao")
    tipo_item = request.form.get("tipo")
    item_idx = int(request.form.get("item_idx"))

    prota = session["prota"]
    inimigo = session["zombie"]
    animal = prota.get("animal") if "animal" in prota else None

    prota, inimigos = aplicar_acao(
        acao, prota, [inimigo], item_idx=item_idx, tipo_item=tipo_item, animal=animal
    )

    session["prota"] = prota
    session["zombie"] = inimigos[0]
    return redirect(url_for("combate"))


if __name__ == "__main__":
    app.run(debug=True)
