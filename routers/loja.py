'''Arquivo para a loja'''
import os
from models.item_catalogo import itens_loja

def acessar_loja(prota, nivel):
    "Função que pergunta se desejar acessar a loja."
    if nivel == 2:
        input("O ar se abriu na sua frente, criando uma espécie de porta...")
        input("De dentro dela saiu um coelho.")
        input("Ele diz ser um vendedor e que tem itens que você possa achar interessante.")
    else:
        input("O coelho vendedor reapareceu.")

    inv = input("Deseja acessar a loja? (S/N): ").lower()
    if inv == "s":
        input("Ok, acessando a loja.")
        os.system("cls")
        show_loja(prota)
    elif inv == "n":
        input("Ok, sem acessar a loja.")
    while inv not in ["s", "n"]:
        print("Entrada inválida. Digite S ou N.")
        inv = input("Deseja acessar a loja? (S/N): ").lower()
        if inv == "s":
            input("Ok, acessando a loja.")
            os.system("cls")
            show_loja(prota)
        elif inv == "n":
            input("Ok, sem acessar a loja.")

def show_loja(prota):
    '''Função que chama a loja'''
    #prota.dinheiro = 150
    retorno = 1
    while retorno != 0:
        print("----------- Loja -----------")
        print(f"O seu dinheiro: ${prota.dinheiro}")
        tipos = {
            "Acessório": [],
            "Arma": [],
            "Armadura": [],
            "Mágico": [],
            "Poção": [],
        }

        lista_itens = []

        for idx, (nome, item) in enumerate(itens_loja.items(), start=1): # pylint: disable=unused-variable
            item.idx = idx  # só funciona se for objeto
            tipos[item.tipo].append(item)
            lista_itens.append(item)

        mapa_indices = []
        contador = 1

        for tipo, itens in tipos.items():
            if itens:
                print(f"\n---- {tipo} ----")
                for item in itens:
                    status = "Comprado" if item in prota.inventario else "Não comprado"
                    preco_info = f"(Preço : ${item.preco})" if item.preco else ""
                    if tipo == "Acessório":
                        print(
                            f"{contador}. {item.nome} - {item.descricao} "
                            f"- Benefício de {item.valor} {item.atributo} "
                            f"{preco_info} ({status})"
                        )
                    elif tipo == "Arma":
                        print(
                            f"{contador}. {item.nome} - {item.descricao} "
                            f"- Dano de {item.dano_min} até {item.dano_max} "
                            f"{preco_info} ({status})"
                        )
                    elif tipo == "Armadura":
                        print(
                            f"{contador}. {item.nome} - {item.descricao} "
                            "- Essa é uma armadura que melhora sua "
                            f"{item.atributo} em {item.valor} "
                            f"{preco_info} ({status})"
                        )
                    elif tipo == "Mágico":
                        print(
                            f"{contador}. {item.nome} - {item.descricao} "
                            f"- Dano de {item.valor} com custo de {item.custo} "
                            f"de energia "
                            f"{preco_info} ({status})"
                        )
                    elif tipo == "Poção":
                        print(
                            f"{contador}. {item.nome} - {item.descricao} "
                            f"- Quantidade: {item.quantidade} "
                            f"- Essa é uma poção para usar no {item.alvo} "
                            f"\ncausando o atributo de {item.atributo} "
                            f"provocando uma quantidade de {item.valor} "
                            f"{preco_info} ({status})"
                        )

                    mapa_indices.append(item)
                    contador += 1

        print("\nDigite o número do equipamento que deseja comprar")
        try:
            retorno = int(input("Pressione 0 para sair da loja: "))
        except ValueError:
            input("Entrada inválida. Pressione Enter para continuar.")
            continue

        if retorno == 0:
            return

        if 1 <= retorno <= len(mapa_indices):
            item_escolhido = mapa_indices[retorno - 1]
            preco = getattr(item_escolhido, "preco", 0)

            if item_escolhido.ativo:
                input("Você já comprou esse item. Pressione Enter para continuar.")
            elif prota.dinheiro >= preco:
                prota.dinheiro -= preco
                item_escolhido.ativo = True
                prota.armazenar_item(item_escolhido)
                input(f"Você comprou {item_escolhido.nome}! Pressione Enter para continuar.")
            else:
                input("Dinheiro insuficiente! Pressione Enter para continuar.")
        else:
            input("Número inválido. Pressione Enter para continuar.")

        os.system("cls")
