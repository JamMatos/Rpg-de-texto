"""Arquivo principal do projeto"""

import os
import json
import routers.conquistas.conquista  # pylint: disable=unused-import
from routers.niveis.primeiro_nivel import primeiro_nivel
from routers.niveis.segundo_nivel import segundo_nivel
from routers.niveis.terceiro_nivel import terceiro_nivel
from routers.niveis.boss_nivel import boss_fight
from routers.inventario import acessar_inventario
from routers.fim_de_jogo import final_do_jogo
from routers.mapa import mostrar_mapa
from routers.loja import acessar_loja
from routers.pato import adotar_pato
from models.jogador import Jogador
from models.item_catalogo import itens
from models.animal_catalogo import pato as pato_pet

CAMINHO_CONQUISTAS = "routers/conquistas/conquistas.json"

# Abrir o json para salvar as conquistas
with open(CAMINHO_CONQUISTAS, "r", encoding="utf-8") as f:
    conquistas = json.load(f)

# Criar o jogador e altera o nome
prota = Jogador()
while prota.nome == "Fulano":
    nome = input("Digite o nome do personagem: ").strip()
    if nome:
        prota.nome = nome.capitalize()
# Definindo inicio do jogo
NIVEL = 1

def verificar_status(jogador: object, nivel: int) -> bool:
    """Função se verificar se o jogo deve continuar ou não."""
    return jogador.vida < 0 and nivel == 0

while prota.vida > 0 and NIVEL != 0:
    os.system("cls")
    input(
        "Você é um jovem fazendeiro cuidando das terras que antes foram dos seus pais, "
        "quando um grupo de monstros atacou \ne sequestraram seu irmão mais novo, Carlos, "
        "e agora você deve criar coragem e ir resgatá-lo."
    )
    input("Ao entrar no covil dos monstros, você pega uma espada de madeira.")
    os.system("cls")

    # Definindo mundo
    prota.armazenar_item(itens["espada_madeira"])
    prota.ativar_item(itens["espada_madeira"])

    mostrar_mapa(NIVEL)
    input(
        "Entrando na primeira câmara você se encontrar com seu primeiro inimigo, um Zumbi."
    )

    os.system("cls")
    while NIVEL == 1:
        resultado = primeiro_nivel(prota, NIVEL)
        NIVEL = resultado

    prota.dinheiro += 30

    input("🎉 Conquista desbloqueada: Matou seu primeiro inimigo!")
    conquistas["primeira_morte"] = True
    with open(CAMINHO_CONQUISTAS, "w", encoding="utf-8") as f:
        json.dump(conquistas, f, indent=4)

    if verificar_status(prota, NIVEL):
        break

    os.system("cls")
    input("Você encontrou um anel de rubi e uma roupa de malha.")
    input("Você encontrou alguns frascos pequenos com um líquido vermelho.")

    prota.armazenar_item(itens["anel_rubi"])
    prota.armazenar_item(itens["peitoral_malha"])
    prota.armazenar_item(itens["pocao_vida_p"])

    acessar_loja(prota, NIVEL)
    acessar_inventario(prota)

    prota.recalcular_status()
    itens["peitoral_malha"].usar_defesa(prota)

    os.system("cls")
    mostrar_mapa(NIVEL)
    input("Entrando na câmara 2, prepare-se.")

    os.system("cls")
    while NIVEL == 2:
        print("Nivel 2")
        resultado = segundo_nivel(prota, NIVEL)
        NIVEL = resultado

    if verificar_status(prota, NIVEL):
        break

    os.system("cls")

    prota.dinheiro += 40
    input(
        "Você encontrou um livro magenta e alguns frascos "
        "com o mesmo líquido vermelho, só que maiores."
    )
    # Adotar o pato
    adotar_pato(prota)

    prota.armazenar_item(itens["king_note"])
    prota.armazenar_item(itens["pocao_vida_g"])

    acessar_loja(prota, NIVEL)
    acessar_inventario(prota)
    prota.recalcular_status()

    os.system("cls")
    mostrar_mapa(NIVEL)
    input("Entrando na câmara 3, prepare-se.")

    os.system("cls")
    while NIVEL == 3:
        print("Nível 3")
        resultado = terceiro_nivel(prota, NIVEL, pato_pet)
        NIVEL = resultado

    if verificar_status(prota, NIVEL):
        break

    if itens["espada_madeira"] in prota.inventario and itens["espada_madeira"].ativo is True:
        input("Parabêns, você derrotou o fantasma usando a espada de madeira.")
        input("Você conseguiu o pingente do macaco.")
        conquistas["fantasma_madeira"] = True
        with open(CAMINHO_CONQUISTAS, "w", encoding="utf-8") as f:
            json.dump(conquistas, f, indent=4)
        prota.armazenar_item(itens["pingente_do_macaco"])

    os.system("cls")

    prota.dinheiro += 40
    input(
        "Ao derrotar o fantasma, ele dropa uma espada prateada brilhante coberta de gosma."
    )
    input("Você também encontrou alguns frascos quadrados com um líquido verde.")
    input("Um novo livro aparece no chão, amarelo com algumas lanças na capa.")

    prota.armazenar_item(itens["espada_fantasma"])
    itens["espada_fantasma"].ativo = False
    prota.armazenar_item(itens["pocao_energia"])
    prota.armazenar_item(itens["gold_rain"])
    acessar_loja(prota, NIVEL)
    acessar_inventario(prota)
    prota.recalcular_status()

    os.system("cls")
    mostrar_mapa(NIVEL)
    input("Entrando na câmara 4, prepare-se.")
    input("Você chegou ao último nível, hora da batalha contra o chefão.")

    os.system("cls")
    while NIVEL == 4:
        print("Boss fight")
        resultado = boss_fight(prota, NIVEL, pato_pet)
        NIVEL = resultado

    if verificar_status(prota, NIVEL):
        break

    # if not conquistas["salvou_irmao"]:
    input("🎉 Conquista desbloqueada: Resgatou seu irmão!")
    conquistas["salvou_irmao"] = True
    with open(CAMINHO_CONQUISTAS, "w", encoding="utf-8") as f:
        json.dump(conquistas, f, indent=4)

    final_do_jogo()
    break
