"""Arquivo com interface de batalha"""

import random
#from models.item import Magico, Pocao
from flask import session
from models.monstros import Zombie, Esqueleto, Fantasma

def aplicar_acao(acao, prota, inimigos:list, item_idx=None, tipo_item=None, animal=None):
    """Executa ação do jogador e depois a reação do inimigo."""
    inimigo = inimigos[0]
    dano_jogador = 0
    dano_inimigo = 0

    # Ataque com arma
    if acao == 1:
        dano_jogador = random.randint(prota["dano_min"], prota["dano_max"])
        inimigo["vida"] -= dano_jogador
        #inimigo.vida -= dano_jogador

    # Ataque com magia (já escolheu a magia)
    elif acao == 2 and tipo_item == "magia" and item_idx is not None:
        magia = prota["inventario"][item_idx]
        if prota["energia"] >= magia["custo"]:
            inimigo["vida"] -= magia["valor"]
            prota["energia"] -= magia["custo"]

    # Usar poção
    elif acao == 3 and tipo_item == "pocao" and item_idx is not None:
        pocao = prota["inventario"][item_idx]
        if pocao["atributo"].lower() == "vida":
            prota["vida"] += pocao["valor"]
        elif pocao["atributo"].lower() == "energia":
            prota["energia"] += pocao["valor"]
        elif pocao["atributo"].lower() == "dano":
            inimigo["vida"] -= pocao["valor"]
        pocao["quantidade"] -= 1

    # Usar pato
    elif acao == 4 and animal:
        inimigo["vida"] = 0

    # Ação do inimigo (se ele ainda estiver vivo)
    if inimigo["vida"] > 0:
        dano_inimigo = random.randint(inimigo["dano_min"], inimigo["dano_max"])
        dano_inimigo -= (prota.get("defesa", 0) / 2)
        prota["vida"] -= max(0, int(dano_inimigo))

    return prota, inimigos, dano_jogador, int(dano_inimigo)

def criar_inimigos_nivel(nivel: int):
    '''Método para criar o monstro do nivel especifico.
    Inputs:
    - nivel: O nivel que deve ser usado'''
    inimigos = []

    if nivel == 1:
        inimigo = Zombie()
        session["inimigo"] = {
            "nome": inimigo.nome,
            "vida": inimigo.vida,
            "dano": inimigo.dano,
            "dano_min": inimigo.dano_min,
            "dano_max": inimigo.dano_max
        }

    elif nivel == 2:
        inimigo = Esqueleto()
        session["inimigo"] = {
            "nome": inimigo.nome,
            "vida": inimigo.vida,
            "dano": inimigo.dano,
            "dano_min": inimigo.dano_min,
            "dano_max": inimigo.dano_max
        }

    elif nivel == 3:
        inimigo = Fantasma()
        session["inimigo"] = {
            "nome": inimigo.nome,
            "vida": inimigo.vida,
            "dano": inimigo.dano,
            "dano_min": inimigo.dano_min,
            "dano_max": inimigo.dano_max
        }
    inimigos.append(session["inimigo"])
    return inimigos
