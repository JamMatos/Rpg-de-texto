"""Arquivo com a primeira fase do jogo."""

import os
from models.monstros import Zombie, Esqueleto
from routers.fim_de_jogo import zerou_vida
#from routers.combate.combate import controles
from routers.combate.interface import interface_batalha, controles


def primeiro_nivel(prota: object, nivel: int):
    """Função que roda o primeiro nível do jogo."""
    zombie = Zombie()
    esqueleto = Esqueleto()
    inimigos = [zombie, esqueleto]
    while zombie.vida > 0 and prota.vida > 0:
        if prota.vida <= 0:
            zerou_vida()
            return None

        os.system("cls")
        interface_batalha(nivel, inimigos, prota)

        novo_nivel: int = controles(prota, inimigos, nivel)
    return novo_nivel
