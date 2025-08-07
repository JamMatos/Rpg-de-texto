'''Arquivo para o último nível do jogo.'''

import os
from models.monstros import ReiCadaver
from routers.fim_de_jogo import zerou_vida
from routers.combate.interface import controles


def boss_fight(prota: object, nivel: int):
    """Função que roda o último nível do jogo."""
    rei = ReiCadaver()
    inimigos = [rei]
    while rei.vida > 0 and prota.vida > 0:
        if prota.vida <= 0:
            zerou_vida()
            return None

        os.system("cls")
        print("----- Boss Fight -----")
        print(f"Inimigo: {rei.nome}")
        print(f"Vida: {rei.vida}")
        print(f"Dano: {rei.dano}\n")

        print(f"Seu nome: {prota.nome}")
        print(f"Vida: {prota.vida}")
        print(f"Dano: {prota.dano}\n")

        novo_nivel: int = controles(prota, inimigos, nivel)
    return novo_nivel
