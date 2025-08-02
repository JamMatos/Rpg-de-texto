#from routers.inicio import prota
from routers.primeiro_nivel import primeiro_nivel
from routers.segundo_nivel import segundo_nivel
from models.jogador import Jogador
import os

prota = Jogador("Fulano", 100, 100, "0", 0, 0)
prota._nome = input("Digite o nome do personagem: ")

while prota.vida > 0 :
    os.system("cls")
    input(f"Você é um jovem fazendeiro cuidando das terras que antes foram dos seus pais, quando um grupo de monstros atacou \ne sequestraram seu irmão mais novo e agora você deve criar coragem e ir resgata-lo.")
    input(f"Ao entrar no covil dos monstros, você pega uma espada de madeira.")
    prota.dano = "5 - 15"
    prota.dano_min = 5
    prota.dano_max = 15
    nivel = 1

    os.system("cls")
    while nivel == 1:
        nivel = primeiro_nivel(prota)

    inv = input("Antes de avançar deseja acessar o inventario: \nS para sim\nN para não")
    if inv.lower("s"):
        pass
    elif inv.lower('n'):
        pass
    else:
        print("Vou acreditar que você errou sem querer.")

    while nivel == 2:
        print("Nivel 2")
        nivel = segundo_nivel()

