'''Arquivo com a primeira fase do jogo.'''
import os
from models.monstros import Zombie
from routers.fim_de_jogo import zerou_vida
from routers.combate import controles

def primeiro_nivel(prota: object, nivel:int):
    '''Função que rodar o primeiro nível do jogo.'''
    zombie = Zombie()
    while zombie.vida > 0 and prota.vida > 0:
        if prota.vida <= 0:
            zerou_vida()

        os.system("cls")
        print("----- Nível 1 -----")
        print(f"Inimigo: {zombie.nome}")
        print(f"Vida: {zombie.vida}")
        print(f"Dano: {zombie.dano}\n")

        print(f"Seu nome: {prota.nome}")
        print(f"Vida: {prota.vida}")
        print(f"Dano: {prota.dano}\n")

        novo_nivel:int = controles(prota, zombie, nivel)
    return novo_nivel
