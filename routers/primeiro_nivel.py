from models.monstros import Zombie
from models.item import Magico, Pocao
from routers.fim_de_jogo import zerou_vida
import random
import os

def primeiro_nivel(prota):
    zombie = Zombie()
    while zombie.vida > 0 and prota.vida > 0:
        if prota.vida <= 0:
            zerou_vida()

        os.system("cls")
        print("----- Nível 1 -----")
        print(f"Inimigo : {zombie}")
        print(f"Vida: {zombie.vida}")
        print(f"Dano: {zombie.dano}\n")

        print(f"Seu nome: {prota._nome}")
        print(f"Vida: {prota.vida}")
        print(f"Dano: {prota.dano}\n")

        print("---- CONTROLES ----")
        print("1 - Atacar com arma")
        if any(isinstance(item, Magico) and item.ativo for item in prota.inventario):
            print("2 - Atacar com magia")
        if any(isinstance(item, Pocao) and item.ativo for item in prota.inventario):
            print("3 - Usar poção")
        try:
            acao = int(input("Digite o número da ação: "))
        except ValueError:
            input("Entrada inválida. Digite apenas números.")
            continue

        if acao == 1:
            dano_jogador = random.randint(prota.dano_min,prota.dano_max)
            zombie.vida -= dano_jogador
            print(f"Você causou um dano de {dano_jogador}.")
            dano_zombie = random.randint(zombie.dano_min,zombie.dano_max)
            prota.vida -= dano_zombie
            input(f"Zombie causou um dano de {dano_zombie}.")

        else:
            input("Ação invalida.")

        if zombie.vida <= 0:
            input("Você completou o primeiro nível.")
            return 2
        
        os.system("cls")