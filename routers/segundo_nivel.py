from models.monstros import Zombie, Esqueleto

import random
import os

def segundo_nivel(prota):
    esqueleto = Esqueleto()
    #zombie = Zombie()

    while esqueleto.vida > 0 and prota.vida > 0:
        os.system("cls")
        print("----- Nível 1 -----")
        print(f"Inimigo : {esqueleto}")
        print(f"Vida: {esqueleto.vida}")
        print(f"Dano: {esqueleto.dano}\n")

        print(f"Seu nome: {prota._nome}")
        print(f"Vida: {prota.vida}")
        print(f"Dano: {prota.dano}\n")

        print("---- CONTROLES ----")
        print("1 - Atacar com arma")
        print("2 - Atacar com magia")
        print("3 - Usar poção")

        try:
            acao = int(input("Digite o número da ação: "))
        except ValueError:
            input("Entrada inválida. Digite apenas números.")
            continue

        if acao == 1:
            dano_jogador = random.randint(prota.dano_min,prota.dano_max)
            esqueleto.vida -= dano_jogador
            print(f"Você causou um dano de {dano_jogador}.")
            dano_esqueleto = random.randint(esqueleto.dano_min,esqueleto.dano_max)
            prota.vida -= dano_esqueleto
            input(f"Esqueleto causou um dano de {dano_esqueleto}.")
        
        elif acao == 2:
            input("Você não possui magias.")

        elif acao == 3:
            input("Você não possui itens.")

        else:
            input("Ação invalida.")


        if esqueleto.vida <= 0:
            input("Você completou o primeiro nível.")
            return 2
        
        os.system("cls")