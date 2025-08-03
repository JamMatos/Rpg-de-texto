import os

def show_inventario(inventario):
    retorno = 1
    while retorno != 0:
        print("----- INVENTÁRIO -----")
        if not inventario:
            print("Seu inventário está vazio.")
        else:
            for idx, item in enumerate(inventario, start=1):
                status = "Equipado" if item.ativo else "Não equipado"
                if item.tipo == "Arma":
                    print("---- Arma ----")
                    print(f"{idx}. {item.nome} - {item.descricao} - Dano de {item.dano_min} até {item.dano_max}  ({status})")
                elif item.tipo == "Acessório":
                    print("\n---- Acessório ----")
                    print(f"{idx}. {item.nome} - {item.descricao} - Benefício de {item.beneficio} ({status})")
        print("\nDigite o número do equipamento que deseja equipar/desequipar")
        try:
            retorno = int(input("Pressione 0 para sair do inventário: "))
        except ValueError:
            input("Entrada inválida. Pressione Enter para continuar.")
            continue

        if retorno == 0:
            return item
        
        # Verifica se retorno é um índice válido
        if 1 <= retorno <= len(inventario):
            item_escolhido = inventario[retorno - 1]
            item_escolhido.ativo = not item_escolhido.ativo
        else:
            input("Número inválido. Pressione Enter para continuar.")

        os.system("cls")

