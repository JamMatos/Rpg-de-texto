"""Arquivo principal do projeto"""

import os
from routers.primeiro_nivel import primeiro_nivel
from routers.segundo_nivel import segundo_nivel
from routers.inventario import show_inventario
from routers.fim_de_jogo import final_do_jogo
from models.jogador import Jogador
from models.item_catalogo import espada_madeira, anel_rubi, KingNote

prota = Jogador()
prota.nome = input("Digite o nome do personagem: ").capitalize()

while prota.vida > 0:
    os.system("cls")
    input(
        "Você é um jovem fazendeiro cuidando das terras que antes foram dos seus pais, " \
        "quando um grupo de monstros atacou \ne sequestraram seu irmão mais novo " \
        "e agora você deve criar coragem e ir resgata-lo."
    )
    input("Ao entrar no covil dos monstros, você pega uma espada de madeira.")

    # Definindo mundo
    espada_madeira.ativo = True
    prota.armazenar_item(espada_madeira)
    KingNote.ativo = True
    prota.armazenar_item(KingNote)
    NIVEL = 1

    os.system("cls")
    # Comentado para fazer o teste do inventario
    while NIVEL == 1:
        prota.dano = "5 - 15"
        NIVEL = primeiro_nivel(prota, NIVEL)
        if prota.vida <= 0:
            break

    os.system("cls")
    input("Você encontrou um anel de rubi.")
    anel_rubi.ativo = True
    prota.armazenar_item(anel_rubi)

    inv = input("Antes de avançar deseja acessar o inventario? (S/N): ").lower()
    if inv == "s":
        input("Ok, acessando o inventário.")
        os.system("cls")
        show_inventario(prota.inventario, prota)
    elif inv == "n":
        input("Ok, sem acessar o inventário.")
    while inv not in ["s", "n"]:
        print("Entrada inválida. Digite S ou N.")
        inv = input("Deseja acessar o inventário? (S/N): ").lower()
        if inv == "s":
            input("Ok, acessando o inventário.")
            os.system("cls")
            show_inventario(prota.inventario, prota)
        elif inv == "n":
            input("Ok, sem acessar o inventário.")

    os.system("cls")
    while NIVEL == 2:
        print("Nivel 2")
        NIVEL = segundo_nivel(prota, NIVEL)
        if prota.vida <= 0:
            break

    prota.armazenar_item(KingNote)

    final_do_jogo()
