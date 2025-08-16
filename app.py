"""Arquivo que roda o jogo no modo web"""

from collections import defaultdict
from flask import Flask, request, render_template, session, redirect, url_for
from models.jogador import Jogador
from models.item_catalogo import itens
from routers.combate.interface_web import aplicar_acao, criar_inimigos_nivel

app = Flask(__name__)
app.secret_key = "segredo123"

@app.route("/")
def index():
    """Método para chamar o caminho principal"""
    return render_template("registro.html")

@app.route("/jogo", methods=["GET", "POST"])
def jogo():
    """Função que capturar o nome do jogador"""
    if "parte" not in session:
        session["parte"] = 1
    parte = session["parte"]
    prota = Jogador()
    prota.nome = request.form.get("nome")
    prota.armazenar_item(itens["espada_madeira"])
    session["espada_madeira"] = {"nome": itens["espada_madeira"].nome}
    session["prota"] = {
        "nome": prota.nome,
        "vida": prota.vida,
        "dano": prota.dano,
        "energia": prota.energia,
        "defesa": prota.defesa,
        "inventario": [item.to_dict() for item in prota.inventario],
        "dano_min": prota.dano_min,
        "dano_max": prota.dano_max,
    }

    if parte >= 2:
        session["anel_rubi"] = {"nome": itens["anel_rubi"].nome}
        session["peitoral_malha"] = {"nome": itens["peitoral_malha"].nome}
        session["pocao_vida_p"] = {"nome": itens["pocao_vida_p"].nome}

        session["peitoral_malha"].usar_defesa(prota)

    if parte >= 3:
        session["king_note"] = {"nome": itens["king_note"].nome}
        session["pocao_vida_g"] = {"nome": itens["pocao_vida_p"].nome}


    return render_template("jogo.html", nome=prota.nome, parte=1)

def verificar_status_protagonista(protagonista):
    """Retorna animal, se tem magia e se tem poção."""
    animal = protagonista.get("animal")
    tem_magia = any(
        i["tipo"] == "Magico" and i["ativo"] for i in protagonista["inventario"]
    )
    tem_pocao = any(
        i["tipo"] == "Pocao" and i["quantidade"] > 0 for i in protagonista["inventario"]
    )
    return animal, tem_magia, tem_pocao

@app.route("/combate/<int:nivel>", methods=["GET", "POST"])
def combate(nivel):
    """Executa o combate do primeiro nível."""
    protagonista = session["prota"]
    parte = nivel

    inimigos = session.get("inimigos")
    # Se for o primeiro acesso ou reset do combate
    if not inimigos: #"inimigos" not in session or session["inimigos"] is None or
        inimigos = criar_inimigos_nivel(nivel)
        session["inimigos"] = inimigos

    #inimigos = session["inimigos"]
    inimigo = inimigos[0]
    vida = inimigo["vida"] if isinstance(inimigo, dict) else inimigo.vida

    if int(vida) <= 0:
        fim_combate(parte)

    animal, tem_magia, tem_pocao = verificar_status_protagonista(protagonista)

    dano_jogador = session.pop("dano_jogador", 0)
    dano_inimigo = session.pop("dano_inimigo", 0)
    acao = session.pop("acao", 0)

    if request.method == "POST":
        acao = int(request.form.get("acao", 0))

        # Redireciona para tela de escolha de magia
        if acao == 2 and tem_magia:
            magias = [
                i
                for i in protagonista["inventario"]
                if i["tipo"] == "Magico" and i["ativo"]
            ]
            return render_template(
                "combate/escolher_item.html", tipo="magia", acao=acao, itens=magias
            )

        # Redireciona para tela de escolha de poção
        if acao == 3 and tem_pocao:
            pocoes = [
                i
                for i in protagonista["inventario"]
                if i["tipo"] == "Pocao" and i["quantidade"] > 0
            ]
            return render_template(
                "combate/escolher_item.html", tipo="pocao", acao=acao, itens=pocoes
            )

        # Aplica ação sem precisar escolher item
        protagonista, inimigos, dano_jogador, dano_inimigo = aplicar_acao(
            acao, protagonista, [inimigo], animal=animal
        )
        session.update({
            "prota": protagonista,
            "inimigos": inimigos,
            "dano_jogador": dano_jogador,
            "dano_inimigo": dano_inimigo,
            "acao": acao,
            "parte": parte,
        })

        vida = inimigos[0]["vida"] if isinstance(inimigos[0], dict) else inimigos[0].vida

        if int(vida) <= 0:
            fim_combate(parte)
        return redirect(url_for("combate", nivel=nivel))

    return render_template(
        "combate/combate.html",
        nivel=nivel,
        prota=protagonista,
        inimigo=inimigo,
        tem_magia=tem_magia,
        tem_pocao=tem_pocao,
        tem_pato=bool(animal),
        dano_jogador=dano_jogador,
        dano_inimigo=dano_inimigo,
        acao=acao,
    )

def fim_combate(nivel: int):
    """Finaliza combate e avança de parte."""
    session.pop("inimigos", None)
    session["parte"] = nivel + 1
    return render_template("jogo.html", parte=nivel+1, nivel=nivel+1)

@app.route("/usar_item", methods=["POST"])
def usar_item():
    """Usa um item (magia ou poção) durante o combate."""
    acao = int(request.form.get("acao", 0))
    tipo_item = request.form.get("tipo")
    item_idx = int(request.form.get("item_idx", 0))

    protagonista = session["prota"]
    inimigo = session["zombie"]
    animal, _, _ = verificar_status_protagonista(protagonista)

    protagonista, inimigos, dano_jogador, dano_inimigo = aplicar_acao(
        acao,
        protagonista,
        [inimigo],
        item_idx=item_idx,
        tipo_item=tipo_item,
        animal=animal,
    )

    session["prota"] = protagonista
    session["zombie"] = inimigos[0]
    session["dano_jogador"] = dano_jogador
    session["dano_inimigo"] = dano_inimigo
    session["acao"] = acao
    return redirect(url_for("combate"))

@app.route("/inventario", methods=["GET","POST"])
def ver_inventario():
    '''Método que chama o inventario'''
    prota_inventario = session["prota"]["inventario"]
    parte = session["parte"]

    grupos = defaultdict(list)
    for item in prota_inventario:
        grupos[item["tipo"]].append(item)

    return render_template("historia/inventario.html", inventario=grupos, parte=parte)

if __name__ == "__main__":
    app.run(debug=True)
