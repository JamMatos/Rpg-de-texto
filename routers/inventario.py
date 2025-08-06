"""Arquivo para o sistema de inventário"""

import os


def show_inventario(inventario, prota):
    """Função que abre o inventário"""
    total_arma = 1
    total_acessorio = 2
    total_magico = 2

    retorno = 1
    while retorno != 0:
        prota.recalcular_status()

        print("----- Seus dados -----")
        print(f"Seu dano: {prota.dano}.")
        print(f"Sua defesa: {prota.defesa}.")
        print(f"Sua vida: {prota.vida}.")
        print("Você só pode equipar uma arma.")
        print("Você só pode equipar até 2 itens acessórios.")
        print("Você só pode equipar até 2 itens mágicos.")
        print()

        print("----- INVENTÁRIO -----")
        if not inventario:
            print("Seu inventário está vazio.")
        else:
            tipos = {
                "Arma": [],
                "Acessório": [],
                "Mágico": [],
                "Poção": [],
            }

            for idx, item in enumerate(inventario, start=1):
                item.idx = idx  # Adiciona índice manualmente para poder reutilizar depois
                tipos[item.tipo].append(item)

            for tipo, itens in tipos.items():
                if itens:
                    print(f"\n---- {tipo} ----")
                    for item in itens:
                        status = "Equipado" if item.ativo else "Não equipado"
                        if tipo == "Arma":
                            print(
                                f"{item.idx}. {item.nome} - {item.descricao} "
                                f"- Dano de {item.dano_min} até {item.dano_max} ({status})"
                            )
                        elif tipo == "Acessório":
                            print(
                                f"{item.idx}. {item.nome} - {item.descricao} "
                                f"- Benefício de {item.valor} {item.atributo} ({status})"
                            )
                        elif tipo == "Mágico":
                            print(
                                f"{item.idx}. {item.nome} - {item.descricao} "
                                f"- Dano de {item.valor} com custo de {item.custo} "
                                f"de energia ({status})"
                            )
                        elif tipo == "Poção":
                            print(
                                f"{item.idx}. {item.nome} - {item.descricao} "
                                f"- Essa é uma poção para usar no {item.alvo} "
                                f"causando o atributo de {item.atributo} "
                                f"provocando uma quantidade de {item.valor} ({status})")

        print("\nDigite o número do equipamento que deseja equipar/desequipar")
        try:
            retorno = int(input("Pressione 0 para sair do inventário: "))
        except ValueError:
            input("Entrada inválida. Pressione Enter para continuar.")
            continue

        if retorno == 0:
            return

        if 1 <= retorno <= len(inventario):
            item_escolhido = inventario[retorno - 1]
            if not item_escolhido.ativo:
                # Verifica limites antes de equipar
                if item_escolhido.tipo == "Arma":
                    if sum(1 for i in inventario if i.tipo == "Arma" and i.ativo) >= total_arma:
                        input("Você já tem uma arma equipada. Desequipe uma para trocar.")
                        continue
                elif item_escolhido.tipo == "Acessório":
                    if sum(1 for i in inventario if i.tipo == "Acessório" and i.ativo) >= total_acessorio:
                        input("Você já tem 2 acessórios equipados. Desequipe um para trocar.")
                        continue
                elif item_escolhido.tipo == "Mágico":
                    if sum(1 for i in inventario if i.tipo == "Mágico" and i.ativo) >= total_magico:
                        input("Você já tem 2 itens mágicos equipados. Desequipe um para trocar.")
                        continue
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
