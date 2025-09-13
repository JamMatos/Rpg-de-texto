"""Arquivo para o sistema de combate"""

import random
import tkinter as tk
from tkinter import IntVar, messagebox # pylint: disable=unused-import

from models.item import Magico, Pocao
from models.monstros import Zombie
from caminhos.entrar import limpar_tela


def primeiro_nivel(prota: object, nivel: int, janela, cont):
    """Função que roda o primeiro nível do jogo. Versão Tkinter."""
    zombie = Zombie()
    inimigos = [zombie]
    novo_nivel = nivel

    limpar_tela(janela)
    #interface_batalha(nivel, janela, inimigos, prota)

    novo_nivel = controles(prota, inimigos, nivel, animal=None, janela=janela, cont=cont)

    if prota.vida <= 0:
        # zerou_vida()
        return 0  # Prota morreu, volta para o nível 0 (ou menu principal)

    return novo_nivel


def interface_batalha(
        nivel: int, janela, inimigos: list, prota: object
    ):
    """Função para criar a Interface das batalhas. Versão Tkinter."""
    if nivel == 4:
        oponente = tk.Label(janela, text="----- Boss Fight -----")
        oponente.config(bg="black", fg="white")
        oponente.pack()
    else:
        oponente = tk.Label(janela, text=f"----- Nível {nivel} -----")
        oponente.config(bg="black", fg="white")
        oponente.pack()
    for idx, inimigo in enumerate(inimigos, start=1):
        if len(inimigos) >= 2:
            tk.Label(janela, text=f"Número inimigo: {idx}.").pack()
        tk.Label(janela, text=f"Inimigo: {inimigo.nome}").pack()
        vida_inimigo = inimigo.vida
        vida_inimigo_label = tk.Label(janela, text=f"Vida: {inimigo.vida}", bg="red")
        vida_inimigo_label.pack()
        vida_inimigo_label.config(text=f"Vida: {inimigo.vida}")
        tk.Label(janela, text=f"Dano: {inimigo.dano}\n").pack()

    prota.recalcular_status("")
    tk.Label(janela, text=f"Seu nome: {prota.nome}").pack()
    vida_prota_label = tk.Label(janela, text=f"Vida: {prota.vida}", bg="orange")
    vida_prota_label.pack()
    vida_prota_label.config(text=f"Vida: {prota.vida}")
    if prota.defesa > 0:
        tk.Label(
            janela, text="# Cada 2 pontos de defesa o dano sofrido diminui em 1."
        ).pack()
        tk.Label(janela, text=f"Defesa: {prota.defesa}").pack()
    tk.Label(janela, text=f"Energia: {prota.energia}").pack()
    tk.Label(janela, text=f"Dano: {prota.dano}\n").pack()
    return vida_inimigo

def acao_inimigo(inimigos: list, prota: object, frame_retorno):
    """Função que executa a ação de combate do inimigo
    
    Inputs:
    - Inimigos: A lista de inimigo que o jogador lutará na fase escolhida.
    - Prota: O objeto jogador.
    - Frame_retorno: A janela onde deve mostrar o resultado do combate."""
    for inimigo in inimigos:
        dano_inimigo = random.randint(inimigo.dano_min, inimigo.dano_max)
        if prota.defesa > 0:
            # Cada 2 pontos de defesa deve diminuir 1 ponto de ataque que o jogador sofre
            # ataque -= (defesa/2)
            dano_inimigo -= prota.defesa / 2
        prota.vida -= dano_inimigo
        if prota.defesa > 0:
            retorno = (
                f"{inimigo.nome} causou um dano de {int(dano_inimigo)} "
                f"({dano_inimigo+(prota.defesa/2)})."
            )
            tk.Label(frame_retorno, text=retorno, bg="red", fg="white").pack()
        else:
            retorno = f"{inimigo.nome} causou um dano de {int(dano_inimigo)}."
            tk.Label(frame_retorno, text=retorno).pack()

def controles(prota: object, inimigos: list, nivel: int, animal: object, janela, cont):
    """Função que chama o sistema de combate. Versão Tkinter"""

    vida_inimigo = interface_batalha(nivel, janela, inimigos, prota)

    magia = False
    pocao = False
    pato = False

    tk.Label(janela, text="---- CONTROLES ----").pack()
    tk.Label(janela, text="1 - Atacar com arma").pack()

    if any(isinstance(item, Magico) and item.ativo for item in prota.inventario):
        magia = True
        tk.Label(janela, text="2 - Atacar com magia").pack()
    if any(isinstance(item, Pocao) and item.ativo for item in prota.inventario):
        pocao = True
        tk.Label(janela, text="3 - Usar poção").pack()
    if prota.vida < 10 and nivel == 4 and animal.ativo is True:
        pato = True
        tk.Label(janela, text="4 - Usar o pato").pack()

    # Frame onde ficam as mensagens de combate
    frame_retorno = tk.Frame(
        janela, bg="White", bd=2, relief="groove", width=100, height=100
    )
    frame_retorno.pack(padx=10, pady=10)

    # No futuro, talvez, eu coloque essa função aqui de volta
    #acao_inimigo()

    def limpar_retorno():
        for widget in frame_retorno.winfo_children():
            widget.destroy()

    def executar_acao(acao: int, inimigo: object):
        sucesso = False
        limpar_retorno()
        if acao == 1:
            dano_jogador = random.randint(prota.dano_min, prota.dano_max)
            inimigo.vida -= dano_jogador
            vida_inimigo -= dano_jogador
            # vida_inimigo_label.config(text=f"Vida: {inimigo.vida}")
            text_retorno = f"Você causou um dano de {dano_jogador}|{inimigo.vida}|{vida_inimigo}."
            retorno = tk.Label(frame_retorno, text=text_retorno)
            retorno.pack()
            retorno.config(bg="Teal", fg="White")
            sucesso = True

        elif acao == 2 and magia is True:
            magias_disponiveis = [
                item
                for item in prota.inventario
                if isinstance(item, Magico) and item.ativo
            ]

            retorno = "\n --- Suas magias ativas ---"
            tk.Label(frame_retorno, text=retorno).pack()
            for idx, magia_item in enumerate(magias_disponiveis, start=1):
                tk.Label(
                    frame_retorno,
                    text=f"{idx}. {magia_item.nome} - {magia_item.descricao}",
                ).pack()
                tk.Label(
                    frame_retorno,
                    text=f"(Dano: {magia_item.valor} | Custo de energia: {magia_item.custo})",
                ).pack()
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
            print(
                f"\nVocê usou {magia_escolhida.nome} e causou {magia_escolhida.valor} de dano."
            )

            sucesso = True

        elif acao == 3 and pocao is True:
            pocoes_disponiveis = [
                item
                for item in prota.inventario
                if isinstance(item, Pocao) and item.ativo and item.quantidade > 0
            ]

            tk.Label(frame_retorno, text="\n --- Suas poçõess ativas ---")
            for idx, pocao_item in enumerate(pocoes_disponiveis, start=1):
                tk.Label(
                    frame_retorno,
                    text=f"{idx}. {pocao_item.nome}" " - {pocao_item.descricao} ",
                )
                tk.Label(frame_retorno, text=f"- {pocao_item.quantidade}")
                tk.Label(
                    frame_retorno,
                    text=f"({pocao_item.atributo.capitalize()}"
                    " | {pocao_item.valor})",
                )

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
                print(
                    f"\nVocê usou {pocao_escolhida.nome} e causou {pocao_escolhida.valor} "
                    f"de {pocao_escolhida.atributo} ao {inimigo.nome}."
                )
            elif pocao_escolhida.atributo == "Vida":
                prota.vida += pocao_escolhida.valor
                print(
                    f"\nVocê usou {pocao_escolhida.nome} e causou {pocao_escolhida.valor} "
                    f"de {pocao_escolhida.atributo} para você."
                )
            elif pocao_escolhida.atributo == "Energia":
                prota.energia += pocao_escolhida.valor
                print(
                    f"\nVocê usou {pocao_escolhida.nome} e causou {pocao_escolhida.valor} "
                    f"de {pocao_escolhida.atributo} para você."
                )

            # Diminuir a quantidade da poção após o uso
            pocao_escolhida.usar()

            sucesso = True

        elif acao == 4 and pato is True:
            tk.Label(
                frame_retorno,
                text="Você, como último recurso, utiliza do pato para atacar.",
            )
            tk.Label(frame_retorno, text="O pato corre em direção ao boss...")
            tk.Label(frame_retorno, text="Então ele tira de debaixo da asa")
            tk.Label(frame_retorno, text="Uma bomba nuclear???")
            limpar_tela(frame_retorno)
            tk.Label(frame_retorno, text="KABOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM!")
            tk.Label(frame_retorno, text=f"{animal.nome} explodiu matando o chefão.")
            inimigo.vida = 0

        if sucesso:
            acao_inimigo(inimigos, prota, frame_retorno)

    # Frame para organizar os botões em grid
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack()

    # Primeira linha
    linha1 = tk.Frame(frame_botoes)
    linha1.pack()
    botao_atacar = tk.Button(
        linha1, text="Atacar com arma", command=lambda: acao_multinimigos(1)
    )
    botao_atacar.pack(side="left", padx=5)
    if pocao is True:
        botao_pocao = tk.Button(
            linha1, text="Usar poção", command=lambda: acao_multinimigos(2)
        )
        botao_pocao.pack(side="left", padx=5)

    # Segunda linha
    linha2 = tk.Frame(frame_botoes)
    linha2.pack()
    if magia is True:
        botao_magia = tk.Button(
            linha2, text="Atacar com magia", command=lambda: acao_multinimigos(3)
        )
        botao_magia.pack(side="left", padx=5)
    if pato is True:
        botao_pato = tk.Button(
            linha2, text="Usar o pato", command=lambda: acao_multinimigos(4)
        )
        botao_pato.pack(side="left", padx=5)

    def acao_multinimigos(acao):
        if acao:
            if len(inimigos) >= 2:
                try:
                    tk.Label(janela, text="Digite qual inimigo deseja atacar: ").pack(
                        pady=5
                    )
                    entrada_escolha = tk.Entry(janela, width=30)
                    entrada_escolha.pack(pady=5)

                    escolha = tk.IntVar()

                    def pegar_escolha():
                        if entrada_escolha.get().strip():
                            try:
                                valor = int(entrada_escolha.get())
                                if 1 <= valor <= len(inimigos):
                                    escolha.set(valor)
                                    inimigo_escolhido = inimigos[escolha.get() - 1]
                                    executar_acao(acao, inimigo_escolhido)
                                else:
                                    messagebox.showwarning(
                                        "Entrada inválida",
                                        f"Digite um número entre 1 e {len(inimigos)}",
                                    )
                            except ValueError:
                                messagebox.showwarning("Erro", "Digite apenas números.")
                                entrada_escolha.config(bg="pink")
                        else:
                            messagebox.showwarning(
                                "Campo Obrigatório", "Por favor, preencha este campo."
                            )
                            entrada_escolha.config(bg="pink")

                    botoa = tk.Button(
                        janela, text="Enviar escolha", command=pegar_escolha
                    )
                    botoa.pack(pady=10)

                except (ValueError, IndexError):
                    tk.Label(
                        janela, text="Escolha inválida. Pressione Enter para continuar"
                    ).pack()

            else:
                inimigo_escolhido = inimigos[0]
                executar_acao(acao, inimigo_escolhido)

    if all(vida_inimigo <= 0 for inimigo in inimigos):
        return nivel + 1, cont + 1
    return nivel, cont
