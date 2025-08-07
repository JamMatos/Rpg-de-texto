"""Arquivo da terceira fase do jogo"""

import os
from models.monstros import Fantasma
from routers.fim_de_jogo import zerou_vida
from routers.combate.interface import controles, interface_batalha


def terceiro_nivel(prota: object, nivel: int):
    """Função que roda o terceiro nível do jogo"""
    fantasma = Fantasma()
    inimigos = [fantasma]
    novo_nivel = nivel

    while fantasma.vida > 0 and prota.vida > 0:
        os.system("cls")
        interface_batalha(nivel, inimigos, prota)

        novo_nivel = controles(prota, inimigos, nivel)

    if prota.vida <= 0:
        zerou_vida()
        return 0  # Prota morreu, acabou o jogo

    return novo_nivel
