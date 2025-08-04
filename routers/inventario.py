"""Arquivo para o sistema de inventário"""

import os


def show_inventario(inventario, prota):
    """Função que abre o inventário"""
    retorno = 1
    while retorno != 0:
        prota.recalcular_status()

        print("----- Seus dados -----")
        print(f"Seu dano: {prota.dano}.")
        print(f"Sua defesa: {prota.defesa}.")
        print(f"Sua vida: {prota.vida}.")
        print()

        print("----- INVENTÁRIO -----")
        if not inventario:
            print("Seu inventário está vazio.")
        else:
            for idx, item in enumerate(inventario, start=1):
                status = "Equipado" if item.ativo else "Não equipado"

                if item.tipo == "Arma":
                    print("---- Arma ----")
                    print(
                        f"{idx}. {item.nome} - {item.descricao} " \
                        f" - Dano de {item.dano_min} até {item.dano_max}  ({status})"
                    )
                elif item.tipo == "Acessório":
                    print("\n---- Acessório ----")
                    print(
                        f"{idx}. {item.nome} - {item.descricao} " \
                        f"- Benefício de {item.valor} {item.atributo} ({status})"
                    )
                elif item.tipo == "Mágico":
                    print("\n---- Mágico ----")
                    print(
                        f"{idx}. {item.nome} - {item.descricao} " \
                        f"- Dano de {item.valor} com custo de {item.custo} de energia ({status})"
                    )
                elif item.tipo == "Poção":
                    print("\n---- Poção ----")
                    print(f"{idx}. {item.nome} - {item.descricao} ({status})")

        print("\nDigite o número do equipamento que deseja equipar/desequipar")
        try:
            retorno = int(input("Pressione 0 para sair do inventário: "))
        except ValueError:
            input("Entrada inválida. Pressione Enter para continuar.")
            continue

        if retorno == 0:
            return

        # Verifica se retorno é um índice válido
        if 1 <= retorno <= len(inventario):
            item_escolhido = inventario[retorno - 1]
            item_escolhido.ativo = not item_escolhido.ativo
        else:
            input("Número inválido. Pressione Enter para continuar.")

        os.system("cls")

def acessar_inventario(prota):
    "Função que pergunta se desejar acessar o inventário."
    inv = input("Antes de avançar deseja acessar o inventário? (S/N): ").lower()
    if inv == "s":
        input("Ok, acessando o inventário.")
        os.system("cls")
        show_inventario(prota.inventario, prota)
    elif inv == "n":
        input("Ok, sem acessar o inventário.")
    while inv not in ["s", "n"]:
        print("Entrada inválida. Digite S ou N.")
        inv = input("Deseja acessar o inventário? (S/N): ").lower()
        if inv == "s":
            input("Ok, acessando o inventário.")
            os.system("cls")
            show_inventario(prota.inventario, prota)
        elif inv == "n":
            input("Ok, sem acessar o inventário.")
