def show_inventario(inventario):
    retorno = 1
    while retorno != 0:
        print("----- INVENTÁRIO -----")
        if not inventario:
            print("Seu inventário está vazio.")
        else:
            for idx, item in enumerate(inventario, start=1):
                status = "Equipado" if item.ativo else "Não equipado"
                print(f"{idx}. {item.nome} - {item.descricao} - Dano de {item.dano_min} até {item.dano_max}  ({status})")
        print("Digite o número do equipamento que deseja equipar")
        retorno = int(input("O que deseja fazer? \nPressione 0 para sair do inventário. "))

