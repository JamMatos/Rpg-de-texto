"""Arquivo com a primeira fase do jogo."""

import os
from models.monstros import Zombie
from routers.fim_de_jogo import zerou_vida
from routers.combate.interface import interface_batalha, controles


def primeiro_nivel(prota: object, nivel: int):
    """Função que roda o primeiro nível do jogo."""

    zombie = Zombie()
    inimigos = [zombie]
    novo_nivel = nivel

    while zombie.vida > 0 and prota.vida > 0:
        os.system("cls")
        interface_batalha(nivel, inimigos, prota)

        novo_nivel = controles(prota, inimigos, nivel, animal=None)

    if prota.vida <= 0:
        zerou_vida()
        return 0  # Prota morreu, volta para o nível 0 (ou menu principal)

    return novo_nivel

def primeiro_nivel_test(prota:object, nivel: int, inimigo: object):
    """Função que roda o primeiro nível do jogo para teste."""

    zombie = inimigo
    inimigos = [zombie]
    novo_nivel = nivel

    while zombie.vida > 0 and prota.vida > 0:
        os.system("cls")
        interface_batalha(nivel, inimigos, prota)

        novo_nivel = controles(prota, inimigos, nivel, animal=None)

    if zombie.vida <= 0:
        novo_nivel = 2

    if prota.vida <= 0:
        #zerou_vida()
        return 0  # Prota morreu, volta para o nível 0 (ou menu principal)

    return novo_nivel
