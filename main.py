"""Arquivo principal do projeto"""

import os
import json
from routers.niveis.primeiro_nivel import primeiro_nivel
from routers.niveis.segundo_nivel import segundo_nivel
from routers.niveis.terceiro_nivel import terceiro_nivel
from routers.niveis.boss_nivel import boss_fight
from routers.inventario import acessar_inventario
from routers.fim_de_jogo import final_do_jogo, zerou_vida
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
    os.system("cls")

    # Definindo mundo
    prota.armazenar_item(espada_madeira)

    NIVEL = 1
    mostrar_mapa(NIVEL)
    input("Entrando na primeira câmara você se encontrar com seu primeiro inimigo, um Zumbi.")

    os.system("cls")
    while NIVEL == 1:
        prota.dano = "10 - 15"
        resultado = primeiro_nivel(prota, NIVEL)
        if resultado is None or prota.vida <= 0:
            zerou_vida()
            break
        else:
            NIVEL = resultado

    if not conquistas["primeira_morte"]:
        print("🎉 Conquista desbloqueada: Matou seu primeiro inimigo!")
        conquistas["primeira_morte"] = True
        with open("../conquistas.json", "w", encoding="utf-8") as f:
            json.dump(conquistas, f, indent=4)

    os.system("cls")
    input("Você encontrou um anel de rubi.")

    prota.armazenar_item(anel_rubi)

    acessar_inventario(prota)

    os.system("cls")
    mostrar_mapa(NIVEL)
    input("Entrando na câmara 2, prepare-se.")

    os.system("cls")
    while NIVEL == 2:
        print("Nivel 2")
        resultado = segundo_nivel(prota, NIVEL)
        if resultado is None or prota.vida <= 0:
            zerou_vida()
            break
        else:
            NIVEL = resultado

    input("Você encontrou um livro magenta e alguns frascos com um líquido vermelho.")

    prota.armazenar_item(KingNote)
    prota.armazenar_item(pocao_vida_p)

    acessar_inventario(prota)

    os.system("cls")
    mostrar_mapa(NIVEL)
    input("Entrando na câmara 3, prepare-se.")

    os.system("cls")
    while NIVEL == 3:
        print("Nível 3")
        resultado = terceiro_nivel(prota, NIVEL)
        if resultado is None or prota.vida <= 0:
            zerou_vida()
            break
        else:
            NIVEL = resultado

    prota.armazenar_item(espada_fantasma)
    espada_fantasma.ativo = False
    acessar_inventario(prota)

    os.system("cls")
    mostrar_mapa(NIVEL)
    input("Entrando na câmara 4, prepare-se.")
    input("Você chegou ao último nível, hora da batalha contra o chefão.")

    os.system("cls")
    while NIVEL == 4:
        print("Boss fight")
        resultado = boss_fight(prota, NIVEL)
        if resultado is None or prota.vida <= 0:
            zerou_vida()
            break
        else:
            NIVEL = resultado

    if not conquistas["salvou_irmao"]:
        print("🎉 Conquista desbloqueada: Resgatou seu irmão!")
        conquistas["salvou_irmao"] = True
        with open("../conquistas.json", "w", encoding="utf-8") as f:
            json.dump(conquistas, f, indent=4)

    final_do_jogo()
    break
