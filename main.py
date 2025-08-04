"""Arquivo principal do projeto"""

import os
import json
from routers.niveis.primeiro_nivel import primeiro_nivel
from routers.niveis.segundo_nivel import segundo_nivel
from routers.niveis.terceiro_nivel import terceiro_nivel
from routers.inventario import acessar_inventario
from routers.fim_de_jogo import final_do_jogo
from routers.mapa import mostrar_mapa
from models.jogador import Jogador
from models.item_catalogo import espada_madeira, anel_rubi, KingNote, espada_fantasma, pocao_vida_p

with open("conquistas.json", "r", encoding="utf-8") as f:
    conquistas = json.load(f)

prota = Jogador()
prota.nome = input("Digite o nome do personagem: ").capitalize()

while prota.vida > 0:
    os.system("cls")
    input(
        "Você é um jovem fazendeiro cuidando das terras que antes foram dos seus pais, "
        "quando um grupo de monstros atacou \ne sequestraram seu irmão mais novo "
        "e agora você deve criar coragem e ir resgatá-lo."
    )
    input("Ao entrar no covil dos monstros, você pega uma espada de madeira.")

    mostrar_mapa(1)
    input("")

    # Definindo mundo
    espada_madeira.ativo = True
    prota.armazenar_item(espada_madeira)

    NIVEL = 1

    os.system("cls")
    # Comentado para fazer o teste do inventario
    while NIVEL == 1:
        prota.dano = "5 - 15"
        NIVEL = primeiro_nivel(prota, NIVEL)
        if prota.vida <= 0:
            break

    if not conquistas["primeira_morte"]:
        print("🎉 Conquista desbloqueada: Matou seu primeiro inimigo!")
        conquistas["primeira_morte"] = True
        with open("../conquistas.json", "w", encoding="utf-8") as f:
            json.dump(conquistas, f, indent=4)

    os.system("cls")
    input("Você encontrou um anel de rubi.")
    anel_rubi.ativo = True
    prota.armazenar_item(anel_rubi)

    acessar_inventario(prota)

    os.system("cls")
    while NIVEL == 2:
        print("Nivel 2")
        NIVEL = segundo_nivel(prota, NIVEL)
        if prota.vida <= 0:
            break

    KingNote.ativo = True
    prota.armazenar_item(KingNote)
    pocao_vida_p.ativo = True
    prota.armazenar_item(pocao_vida_p)

    acessar_inventario(prota)

    while NIVEL == 3:
        print("Nível 3")
        NIVEL = terceiro_nivel(prota, NIVEL)
        if prota.vida <= 0:
            break

    espada_fantasma.ativo = True
    prota.armazenar_item(espada_fantasma)

    acessar_inventario(prota)

    final_do_jogo()
