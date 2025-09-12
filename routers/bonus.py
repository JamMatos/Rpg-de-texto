"""Arquivo para ficar os itens especiais secretos"""
import random
def espelho(prota: object):
    "Função para o objeto Espelho do tipo Místico"
    prota.vida = random.randint(1, 120)
    prota.dano_min = random.randint(10, 40)
    prota.dano_max = random.randint(20,40)
    prota.defesa = random.randint(10,30)
    prota.energia = random.randint(80, 140)
