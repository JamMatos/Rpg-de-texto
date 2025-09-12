"""Arquivo com o layout do mapa. Versão Tkinter"""
import tkinter as tk

def mostrar_mapa_tk(sala: int, janela):
    """Mostra o mapa com o jogador na sala atual (1 a 4) Versão Tkinter"""

    # Limpa janela antes de desenhar o mapa de novo
    for widget in janela.winfo_children():
        widget.destroy()

    # Mapeia as salas para suas posições visuais
    posicoes = {
        1: ("()", "  ", "  ", "  "),
        2: ("  ", "()", "  ", "  "),
        3: ("  ", "  ", "()", "  "),
        4: ("  ", "  ", "  ", "()"),
    }

    jo1, jo2, jo3, jo4 = posicoes.get(
        sala, ("  ", "  ", "  ", "  ")
    )  # fallback se sala inválida

    mapa = [
        "|¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|",
        f"|                 {jo2}             |   |¯¯|                   |",
        "|          |_________________  __|_____                     |",
        f"|    {jo1}    |                           |                    |",
        f"|          |                           |        {jo4}          |",
        f"|          |           {jo3}                                   |",
        "|____  ____|___________________________|____________________|",
    ]

    # Mostra o mapa principal
    mapa_texto = "\n".join(mapa)
    mapa_label = tk.Label(
        janela,
        text=mapa_texto,
        font=("Courier", 10),
        bg="black",
        fg="white",
        justify="left"
    )
    mapa_label.pack(pady=10)

    # Texto de localização
    localizacao = tk.Label(
        janela,
        text="--- Onde você se encontra é representado pelo símbolo () ---",
        font=("Courier", 10),
        bg="black",
        fg="lightgray"
    )
    localizacao.pack(pady=5)

    salas = {
        1: [
            "\n---------------------- Primeira câmara ----------------------",
            " /       |                                         |       \\ ",
            "/        |                                         |  |¯¯|  \\",
            "|        |                                         |  |  |  |",
            "|        |            /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\\            |  |  |  |",
            "|        |           /                 \\           |  |  |  |",
            "|        |          /                   \\          |  |  |  |",
            "|        |         /                     \\         |  |  |  |",
            "|        |        ||    (@)       (@)    ||        |  |  |  |",
            "|        |        ||                     ||        |  |  |  |",
            "|        |________||                     ||________|  |  |  |",
            "|        /        ||                     ||        \\  |  |  |",
            "|       /          \\                     /          \\ |  |  |",
            "|      /            \\    >--------<     /            \\|  |  |",
            "|     /              \\                 /              \\  |  |",
            "|    /                \\_______________/                \\ |  |",
            "|   /                                                   \\|  |",
            "|  /                                                     \\  |",
            "| /                                                       \\ |",
            "|/_________________________________________________________\\|",
        ],
        2: [
            "\n---------------------- Segunda câmara ----------------------",
        ],
        3: [
            "\n---------------------- Terceira câmara ----------------------",
        ],
        4: [
            "\n---------------------- Quarta câmara ----------------------",
        ],
    }
    camara = salas.get(sala)
    if camara:
        camara_texto = "\n".join(camara)
        camara_label = tk.Label(
            janela,
            text=camara_texto,
            font=("Courier", 10),
            bg="black",
            fg="lightgray",
            justify="left"
        )
        camara_label.pack(pady=10)
