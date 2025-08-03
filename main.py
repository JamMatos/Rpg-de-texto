from routers.primeiro_nivel import primeiro_nivel
from routers.segundo_nivel import segundo_nivel
from routers.inventario import show_inventario
from routers.fim_de_jogo import final_do_jogo
from models.jogador import Jogador
from models.item_catalogo import espada_madeira, anel_rubi
import os

prota = Jogador()
prota._nome = input("Digite o nome do personagem: ").capitalize()

while prota.vida > 0 :
    os.system("cls")
    input(f"Você é um jovem fazendeiro cuidando das terras que antes foram dos seus pais, quando um grupo de monstros atacou \ne sequestraram seu irmão mais novo e agora você deve criar coragem e ir resgata-lo.")
    input(f"Ao entrar no covil dos monstros, você pega uma espada de madeira.")

    # Definindo mundo
    espada_madeira.ativo = True
    prota.equipar_item(espada_madeira)
    prota.dano = "5 - 15"
    prota.dano_min += espada_madeira.dano_min
    prota.dano_max += espada_madeira.dano_max
    nivel = 1

    os.system("cls")
    #Comentado para fazer o teste do inventario
    while nivel == 1:
        nivel = primeiro_nivel(prota)
        if prota.vida <= 0:
            break

    anel_rubi.ativo = True
    prota.equipar_item(anel_rubi)
    inv = input("Antes de avançar deseja acessar o inventario? (S/N): ").lower()
    if inv == "s":
        input("Ok, acessando o inventário.")
        os.system("cls")
        show_inventario(prota.inventario)
    elif inv == "n":
        input("Ok, sem acessar o inventário.")
    while inv not in ["s","n"]:
        print("Entrada inválida. Digite S ou N.")
        inv = input("Deseja acessar o inventário? (S/N): ").lower()
        if inv == "s":
            input("Ok, acessando o inventário.")
            os.system("cls")
            show_inventario(prota.inventario)
        elif inv == "n":
            input("Ok, sem acessar o inventário.")

    os.system("cls")
    while nivel == 2:
        print("Nivel 2")
        nivel = segundo_nivel(prota)

    final_do_jogo()