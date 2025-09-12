'''Arquivo com interface de batalha'''
import random
import os
from models.item import Magico, Pocao

def interface_batalha(nivel:int, inimigos: list, prota: object):
    '''Função para criar a Interface das batalhas.'''
    if nivel == 4:
        print("----- Boss Fight -----")
    else:
        print(f"----- Nível {nivel} -----")
    for idx, inimigo in enumerate(inimigos, start=1):
        if len(inimigos) >= 2:
            print(f"Número inimigo: {idx}.")
        print(f"Inimigo: {inimigo.nome}")
        print(f"Vida: {inimigo.vida}")
        print(f"Dano: {inimigo.dano}\n")

    prota.recalcular_status("")
    print(f"Seu nome: {prota.nome}")
    print(f"Vida: {prota.vida}")
    if prota.defesa > 0:
        print("# Cada 2 pontos de defesa o dano sofrido diminui em 1.")
        print(f"Defesa: {prota.defesa}")
    print(f"Energia: {prota.energia}")
    print(f"Dano: {prota.dano}\n")


def controles(prota, inimigos: list, nivel:int, animal: object):
    '''Função que chama o sistema de combate.'''

    magia = False
    pocao = False
    pato = False

    print("---- CONTROLES ----")
    print("1 - Atacar com arma")

    if any(isinstance(item, Magico) and item.ativo for item in prota.inventario):
        magia = True
        print("2 - Atacar com magia")
    if any(isinstance(item, Pocao) and item.ativo for item in prota.inventario):
        pocao = True
        print("3 - Usar poção")
    if prota.vida < 10 and nivel == 4 and animal.ativo is True:
        pato = True
        print("4 - Usar o pato")

    def acao_inimigo():
        for inimigo in inimigos:
            dano_inimigo = random.randint(inimigo.dano_min,inimigo.dano_max)
            if prota.defesa > 0:
                # Cada 2 pontos de defesa deve diminuir 1 ponto de ataque que o jogador sofre
                #ataque -= (defesa/2)
                dano_inimigo -= (prota.defesa/2)
            prota.vida -= dano_inimigo
            if prota.defesa > 0:
                input(f"{inimigo.nome} causou um dano de {int(dano_inimigo)} "
                f"({dano_inimigo+(prota.defesa/2)}).")
            else:
                input(f"{inimigo.nome} causou um dano de {int(dano_inimigo)}.")

    def executar_acao(acao,inimigo):
        sucesso = False
        if acao == 1:
            dano_jogador = random.randint(prota.dano_min,prota.dano_max)
            inimigo.vida -= dano_jogador
            print(f"Você causou um dano de {dano_jogador}.")
            sucesso = True

        elif acao == 2 and magia is True:
            magias_disponiveis = [item for item in prota.inventario \
            if isinstance(item, Magico) and item.ativo]

            print("\n --- Suas magias ativas ---")
            for idx, magia_item in enumerate(magias_disponiveis, start=1):
                print(f"{idx}. {magia_item.nome} - {magia_item.descricao}")
                print(f"(Dano: {magia_item.valor} | Custo de energia: {magia_item.custo})")

            try:
                escolha = int(input("Escolha a magia que deseja usar: "))
                if escolha == 0:
                    input("Você decidiu não usar magias.")
                    return
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

            sucesso = True

        elif acao == 3 and pocao is True:
            pocoes_disponiveis = [item for item in prota.inventario \
            if isinstance(item, Pocao) and item.ativo and item.quantidade > 0]

            print("\n --- Suas poçõess ativas ---")
            for idx, pocao_item in enumerate(pocoes_disponiveis, start=1):
                print(f"{idx}. {pocao_item.nome} - {pocao_item.descricao} ")
                print(f"- {pocao_item.quantidade}")
                print(f"({pocao_item.atributo.capitalize()} | {pocao_item.valor})")

            try:
                escolha = int(input("Escolha a poção que deseja usar: "))
                if escolha == 0:
                    input("Você decidiu não usar nenhuma poção.")
                    return

                pocao_escolhida = pocoes_disponiveis[escolha - 1]
            except (ValueError, IndexError):
                input("Escolha inválida. Pressione Enter para continuar")
                return

            if pocao_escolhida.atributo == "Dano":
                inimigo.vida -= pocao_escolhida.valor
                print(f"\nVocê usou {pocao_escolhida.nome} e causou {pocao_escolhida.valor} "
                f"de {pocao_escolhida.atributo} ao {inimigo.nome}.")
            elif pocao_escolhida.atributo == "Vida":
                prota.vida += pocao_escolhida.valor
                print(f"\nVocê usou {pocao_escolhida.nome} e causou {pocao_escolhida.valor} "
                f"de {pocao_escolhida.atributo} para você.")
            elif pocao_escolhida.atributo == "Energia":
                prota.energia += pocao_escolhida.valor
                print(f"\nVocê usou {pocao_escolhida.nome} e causou {pocao_escolhida.valor} "
                f"de {pocao_escolhida.atributo} para você.")

            #Diminuir a quantidade da poção após o uso
            pocao_escolhida.usar()

            sucesso = True

        elif acao == 4 and pato is True:
            input("Você, como último recurso, utiliza do pato para atacar.")
            input("O pato corre em direção ao boss...")
            input("Então ele tira de debaixo da asa")
            input("Uma bomba nuclear???")
            os.system("cls")
            input("KABOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM!")
            input(f"{animal.nome} explodiu matando o chefão.")
            inimigo.vida = 0

        if sucesso:
            acao_inimigo()

    acao = None

    try:
        acao = int(input("Digite o número da ação: "))
        if acao < 1: # or acao > len(inimigos):
            input("Entrada inválida. Digite apenas ações possíveis")
    except ValueError:
        input("Entrada inválida. Digite apenas ações possíveis")

    if acao:
        if len(inimigos) >= 2 and acao:
            try:
                escolha = int(input("Qual inimigo deseja atacar? "))
                inimigo_escolhido = inimigos[escolha - 1]

                if escolha < 1 or escolha > len(inimigos):
                    input("Entrada inválida. Digite apenas ações possíveis")

                if acao and escolha:
                    executar_acao(acao, inimigo_escolhido)
            except (ValueError, IndexError):
                input("Escolha inválida. Pressione Enter para continuar")

        else:
            inimigo_escolhido = inimigos[0]
            executar_acao(acao, inimigo_escolhido)

    if all(inimigo.vida <= 0 for inimigo in inimigos):
        return nivel + 1
    return nivel
