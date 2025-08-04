'''Arquivo com a segunda fase do jogo.'''
import os
from models.monstros import Esqueleto
from routers.fim_de_jogo import zerou_vida
from routers.combate import controles

def segundo_nivel(prota: object, nivel:int):
    '''Função que rodar o segundo nível do jogo. '''
    esqueleto = Esqueleto()
    while esqueleto.vida > 0 and prota.vida > 0:
        if prota.vida <= 0:
            zerou_vida()

        os.system("cls")
        print("----- Nível 2 -----")
        print(f"Inimigo : {esqueleto.nome}")
        print(f"Vida: {esqueleto.vida}")
        print(f"Dano: {esqueleto.dano}\n")

        print(f"Seu nome: {prota.nome}")
        print(f"Vida: {prota.vida}")
        print(f"Dano: {prota.dano}\n")

        novo_nivel:int = controles(prota, esqueleto, nivel)
    return novo_nivel
