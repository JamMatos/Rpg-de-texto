"""Arquivo para testar GUI"""

import tkinter as tk
from caminhos.combate import primeiro_nivel
from caminhos.entrar import registro, fluxo, limpar_tela  # pylint: disable=import-error
from caminhos.mapa import mostrar_mapa_tk
from models.jogador import Jogador
from models.item_catalogo import itens

prota = Jogador()
prota.nome = registro() #pylint: disable=E1111

def verificar_status(jogador: object, nivel: int) -> bool:
    """Função para verificar status do jogo"""
    return jogador.vida <= 0 or nivel == 0


def aumentar():
    """Avança a história"""
    CONT.set(CONT.get() + 1)
    atualizar_fluxo()


def continuar():
    """Função que cria o botão para avançar a história"""
    return tk.Button(janela, text="Continuar", command=aumentar)


def atualizar_fluxo():
    """Gerencia os passos da história"""
    if verificar_status(prota, NIVEL.get()):
        janela.quit()
        return

    cont = CONT.get()

    if cont == 1:
        fluxo(janela, 1)
        prota.armazenar_item(itens["espada_madeira"])
        prota.ativar_item(itens["espada_madeira"])
        botao()
    elif cont == 2:
        mostrar_mapa_tk(NIVEL.get(), janela)
        fluxo(janela, 2)
        botao()
    elif cont == 3:
        limpar_tela(janela)
        fluxo(janela, 3)
        #botao()
        # Combate nivel 1
        botao2 = tk.Button(
            janela, text="Lutar", command=lambda: primeiro_nivel(prota, NIVEL.get(), janela, CONT)
        )
        botao2.pack(pady=10)
    elif cont == 4:
        limpar_tela(janela)
        fluxo(janela, 4)


def botao():
    """Função que criar o botão para avançar"""
    btn = continuar()
    btn.pack()


while prota.vida > 0:
    janela = tk.Tk()
    janela.title("Jogo")
    janela.geometry("800x800")
    janela.config(bg="black")

    NIVEL = tk.IntVar(value=1)
    CONT = tk.IntVar(value=1)

    atualizar_fluxo()
    janela.mainloop()

    break
