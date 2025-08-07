'''Arquivo com a segunda fase do jogo.'''
import os
from models.monstros import Esqueleto
from routers.fim_de_jogo import zerou_vida
from routers.combate.interface import interface_batalha, controles

def segundo_nivel(prota: object, nivel:int):
    '''Função que rodar o segundo nível do jogo. '''

    esqueleto = Esqueleto()
    inimigos = [esqueleto]
    novo_nivel = nivel

    while esqueleto.vida > 0 and prota.vida > 0:
        os.system("cls")
        interface_batalha(nivel, inimigos, prota)

        novo_nivel = controles(prota, inimigos, nivel)

    if prota.vida <= 0:
        zerou_vida()
        return 0  # Prota morreu, acabou o jogo

    return novo_nivel
