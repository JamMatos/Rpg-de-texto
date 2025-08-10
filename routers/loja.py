'''Arquivo para a loja'''
import os
from models.item_catalogo import itens_loja

def loja(prota):
    '''Função que chama a loja'''
    retorno = 1
    while retorno != 0:
        print("----------- Loja -----------")
        tipos = {
            "Arma": [],
            "Acessório": [],
            "Mágico": [],
            "Poção": [],
            "Armadura": [],
        }

        lista_itens = []

        for idx, (nome, item) in enumerate(itens_loja.items(), start=1):
            item.idx = idx  # só funciona se for objeto
            tipos[item.tipo].append(item)

        for tipo, itens in tipos.items():
            if itens:
                print(f"\n---- {tipo} ----")
                for item in itens:
                    status = "Comprado" if item.ativo else "Não comprado"
                    preco_info = f"(Preço : {item.preco})" if item.preco else ""
                    if tipo == "Arma":
                        print(
                            "Preço: "
                            f"{item.idx}. {item.nome} - {item.descricao} "
                            f"- Dano de {item.dano_min} até {item.dano_max} "
                            f"{preco_info} ({status})"
                        )
                    elif tipo == "Acessório":
                        print(
                            f"{item.idx}. {item.nome} - {item.descricao} "
                            f"- Benefício de {item.valor} {item.atributo} "
                            f"{preco_info} ({status})"
                        )
                    elif tipo == "Mágico":
                        print(
                            f"{item.idx}. {item.nome} - {item.descricao} "
                            f"- Dano de {item.valor} com custo de {item.custo} "
                            f"de energia "
                            f"{preco_info} ({status})"
                        )
                    elif tipo == "Poção":
                        print(
                            f"{item.idx}. {item.nome} - {item.descricao} "
                            f"- Quantidade: {item.quantidade} "
                            f"- Essa é uma poção para usar no {item.alvo} "
                            f"\ncausando o atributo de {item.atributo} "
                            f"provocando uma quantidade de {item.valor} "
                            f"{preco_info} ({status})"
                        )
                    elif tipo == "Armadura":
                        print(
                            f"{item.idx}. {item.nome} - {item.descricao} "
                            "- Essa é uma armadura que melhora sua "
                            f"{item.atributo} em {item.valor} "
                            f"{preco_info} ({status})"
                        )

        print("\nDigite o número do equipamento que deseja comprar")
        try:
            retorno = int(input("Pressione 0 para sair da loja: "))
        except ValueError:
            input("Entrada inválida. Pressione Enter para continuar.")
            continue

        if retorno == 0:
            return

        if 1 <= retorno <= len(lista_itens):
            item_escolhido = lista_itens[retorno - 1]
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
