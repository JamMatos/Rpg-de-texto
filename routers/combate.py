'''Arquivo para ficar o sistema de combate'''
import random
from models.item import Magico, Pocao

def controles(prota, inimigo, nivel:int):
    '''Função que chama o sistema de combate.'''
    magia = False
    pocao = False
    print("---- CONTROLES ----")
    print("1 - Atacar com arma")
    if any(isinstance(item, Magico) and item.ativo for item in prota.inventario):
        magia = True
        print("2 - Atacar com magia")
    if any(isinstance(item, Pocao) and item.ativo for item in prota.inventario):
        pocao = True
        print("3 - Usar poção")

    try:
        acao = int(input("Digite o número da ação: "))
    except ValueError:
        acao = input("Entrada inválida. Digite apenas números.")

    if acao == 1:
        dano_jogador = random.randint(prota.dano_min,prota.dano_max)
        inimigo.vida -= dano_jogador
        print(f"Você causou um dano de {dano_jogador}.")
        dano_inimigo = random.randint(inimigo.dano_min,inimigo.dano_max)
        prota.vida -= dano_inimigo
        input(f"{inimigo.nome} causou um dano de {dano_inimigo}.")

    if acao == 2 and magia:
        magias_disponiveis = [item for item in prota.inventario if isinstance(item, Magico) and item.ativo]

        print("\n --- Suas magias ativas ---")
        for idx, magia_item in enumerate(magias_disponiveis, start=1):
            print(f"{idx}. {magia_item.nome} - {magia_item.descricao}")
            print(f"   ➤ Dano: {magia_item.valor} | Custo de energia: {magia_item.custo}")

        try:
            escolha = int(input("Escolha a magia que deseja usar: "))
            magia_escolhida = magias_disponiveis[escolha - 1]
        except (ValueError, IndexError):
            input("Escolha inválida. Pressione Enter para continuar")
            return

        if prota.energia < magia_escolhida.custo:
            input("Você não tem energia suficiente para usar essa magia.")
            return

        inimigo.vida -= magia_escolhida.valor
        prota.energia -= magia_escolhida.custo
        print(f"\nVocê usou {magia_escolhida.nome} e causou {magia_escolhida.valor} de dano.")

        dano_inimigo = random.randint(inimigo.dano_min,inimigo.dano_max)
        prota.vida -= dano_inimigo
        input(f"{inimigo.nome} causou um dano de {dano_inimigo}.")

    if acao == 3 and pocao:
        dano_inimigo = random.randint(inimigo.dano_min,inimigo.dano_max)
        prota.vida -= dano_inimigo
        input(f"{inimigo.nome} causou um dano de {dano_inimigo}.")

    if inimigo.vida <= 0:
        novo_nivel = nivel + 1
        return novo_nivel
