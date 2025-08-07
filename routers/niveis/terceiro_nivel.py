"""Arquivo da terceira fase do jogo"""

import os
from models.monstros import Fantasma
from routers.fim_de_jogo import zerou_vida
from routers.combate.combate import controles


def terceiro_nivel(prota: object, nivel: int):
    """Função que roda o terceiro nível do jogo"""
    fantasma = Fantasma()
    while fantasma.vida > 0 and prota.vida > 0:
        if prota.vida <= 0:
            zerou_vida()

        os.system("cls")
        print("----- Nível 3 -----")
        print(f"Inimigo: {fantasma.nome}")
        print(f"Vida: {fantasma.vida}")
        print(f"Dano: {fantasma.dano}\n")

        print(f"Seu nome: {prota.nome}")
        print(f"Vida: {prota.vida}")
        print(f"Dano: {prota.dano}\n")

        novo_nivel: int = controles(prota, fantasma, nivel)
    return novo_nivel
