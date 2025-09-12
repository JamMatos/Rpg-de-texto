"""Arquivo para o sistema de combate"""
import tkinter as tk

from models.monstros import Zombie
from caminhos.entrar import limpar_tela

def primeiro_nivel(prota: object, nivel: int, janela):
    """Função que roda o primeiro nível do jogo. Versão Tkinter."""
    zombie = Zombie()
    inimigos = [zombie]
    novo_nivel = nivel

    limpar_tela(janela)
    interface_batalha(nivel, inimigos, prota, janela)

    #novo_nivel = controles(prota, inimigos, nivel, animal=None)

    if prota.vida <= 0:
        #zerou_vida()
        return 0  # Prota morreu, volta para o nível 0 (ou menu principal)

    return novo_nivel

def interface_batalha(nivel:int, inimigos:list, prota: object, janela):
    '''Função para criar a Interface das batalhas. Versão Tkinter.'''
    if nivel == 4:
        oponente = tk.Label(janela,text="----- Boss Fight -----")
        oponente.config(bg="black", fg="white")
        oponente.pack()
    else:
        oponente = tk.Label(janela,text=f"----- Nível {nivel} -----")
        oponente.config(bg="black", fg="white")
        oponente.pack()
    for idx, inimigo in enumerate(inimigos, start=1):
        if len(inimigos) >= 2:
            tk.Label(janela, text=f"Número inimigo: {idx}.").pack()
        tk.Label(janela,text=f"Inimigo: {inimigo.nome}").pack()
        tk.Label(janela,text=f"Vida: {inimigo.vida}").pack()
        tk.Label(janela,text=f"Dano: {inimigo.dano}\n").pack()

    prota.recalcular_status("")
    tk.Label(janela,text=f"Seu nome: {prota.nome}").pack()
    tk.Label(janela,text=f"Vida: {prota.vida}").pack()
    if prota.defesa > 0:
        tk.Label(janela,text="# Cada 2 pontos de defesa o dano sofrido diminui em 1.").pack()
        tk.Label(janela,text=f"Defesa: {prota.defesa}").pack()
    tk.Label(janela,text=f"Energia: {prota.energia}").pack()
    tk.Label(janela,text=f"Dano: {prota.dano}\n").pack()
