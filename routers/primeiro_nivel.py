from models.monstros import Zombie
#from routers.inicio import prota
import random
import os

def primeiro_nivel(prota):
    zombie = Zombie()
    while zombie.vida > 0 and prota.vida > 0:
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
        print("2 - Atacar com magia")
        print("3 - Usar item")
        try:
            acao = int(input("Digite o número da ação: "))
        except ValueError:
            input("Entrada inválida. Digite apenas números.")
            continue

        if acao == 1:
            dano_jogador = random.randint(prota.dano_min,prota.dano_max)
            zombie.vida -= dano_jogador
            print(f"Você causou um dano de {dano_jogador}.")
            dano_zombie = random.randint(9,14)
            prota.vida -= dano_zombie
            input(f"Zombie causou um dano de {dano_zombie}.")
        
        elif acao == 2:
            input("Você não possui magias.")

        elif acao == 3:
            input("Você não possui itens.")

        else:
            input("Ação invalida.")

        if prota.vida <= 0:
            input("Você falhou em salvar seu irmão.")
            break

        if zombie.vida <= 0:
            input("Você completou o primeiro nivel.")
            return 2
        
        os.system("cls")
