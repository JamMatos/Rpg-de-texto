"""Arquivo com o layout do mapa."""


def mostrar_mapa(sala):
    """Função que criar o mapa das salas"""
    jo1 = ""
    jo2 = ""
    jo3 = ""
    jo4 = ""

    if sala == 1:
        jo1 = "()"
        jo2 = "  "
        jo3 = "  "
        jo4 = "  "

    mapa = [
        "|¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|",
        f"|                 {jo2}             |   |¯¯|                   |",
        "|          |_________________  __|_____                     |",
        f"|    {jo1}    |                           |                    |",
        f"|          |                           |        {jo4}          |",
        f"|          |           {jo3}                                   |",
        "|____  ____|___________________________|____________________|",
    ]

    for linha in mapa:
        print(linha)
