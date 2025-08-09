"""Arquivo principal do projeto"""

import os
import json
from routers.niveis.primeiro_nivel import primeiro_nivel
from routers.niveis.segundo_nivel import segundo_nivel
from routers.niveis.terceiro_nivel import terceiro_nivel
from routers.niveis.boss_nivel import boss_fight
from routers.inventario import acessar_inventario
from routers.fim_de_jogo import final_do_jogo
from routers.mapa import mostrar_mapa
from models.jogador import Jogador
from models.item_catalogo import (
    espada_madeira,
    anel_rubi,
    KingNote,
    espada_fantasma,
    pocao_vida_p,
    pocao_vida_g,
    peitoral_malha,
)

with open("../conquistas.json", "r", encoding="utf-8") as f:
    conquistas = json.load(f)

prota = Jogador()
while prota.nome == "Fulano":
    nome = input("Digite o nome do personagem: ").strip()
    if nome:
        prota.nome = nome.capitalize()
NIVEL = 1


def verificar_status(jogador: object, nivel: int) -> bool:
    """Função se verificar se o jogo deve continuar ou não."""
    return jogador.vida < 0 and nivel == 0


while prota.vida > 0 and NIVEL != 0:
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
    # prota.dano = "10 - 15"

    mostrar_mapa(NIVEL)
    input(
        "Entrando na primeira câmara você se encontrar com seu primeiro inimigo, um Zumbi."
    )

    os.system("cls")
    while NIVEL == 1:
        resultado = primeiro_nivel(prota, NIVEL)
        NIVEL = resultado
    if not conquistas["primeira_morte"]:
        print("🎉 Conquista desbloqueada: Matou seu primeiro inimigo!")
        conquistas["primeira_morte"] = True
        with open("../conquistas.json", "w", encoding="utf-8") as f:
            json.dump(conquistas, f, indent=4)

    if verificar_status(prota, NIVEL):
        break

    os.system("cls")
    input("Você encontrou um anel de rubi e uma roupa de malha.")

    prota.armazenar_item(anel_rubi)
    prota.armazenar_item(peitoral_malha)
    prota.armazenar_item(pocao_vida_p)

    acessar_inventario(prota)
    prota.recalcular_status()
    peitoral_malha.usar_defesa(prota)

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

    input("Você encontrou um livro magenta e alguns frascos com um líquido vermelho.")

    prota.armazenar_item(KingNote)
    prota.armazenar_item(pocao_vida_g)

    acessar_inventario(prota)
    prota.recalcular_status()

    os.system("cls")
    mostrar_mapa(NIVEL)
    input("Entrando na câmara 3, prepare-se.")

    os.system("cls")
    while NIVEL == 3:
        print("Nível 3")
        resultado = terceiro_nivel(prota, NIVEL)
        NIVEL = resultado

    if verificar_status(prota, NIVEL):
        break

    prota.armazenar_item(espada_fantasma)
    espada_fantasma.ativo = False
    acessar_inventario(prota)
    prota.recalcular_status()

    os.system("cls")
    mostrar_mapa(NIVEL)
    input("Entrando na câmara 4, prepare-se.")
    input("Você chegou ao último nível, hora da batalha contra o chefão.")

    os.system("cls")
    while NIVEL == 4:
        print("Boss fight")
        resultado = boss_fight(prota, NIVEL)
        NIVEL = resultado

    if not conquistas["salvou_irmao"]:
        print("🎉 Conquista desbloqueada: Resgatou seu irmão!")
        conquistas["salvou_irmao"] = True
        with open("../conquistas.json", "w", encoding="utf-8") as f:
            json.dump(conquistas, f, indent=4)

    if verificar_status(prota, NIVEL):
        break

    final_do_jogo()
    break
