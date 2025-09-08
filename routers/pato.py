"""Arquivo com código relacionado a chamar o pato"""

from models.animal_catalogo import pato as pato_pet


def adotar_pato(prota):
    """Função para adoção do pato"""
    adotar = input(
        "Saindo da câmara, você encontra um pato preso.\nDeseja adotá-lo? (S/N) "
    ).lower()
    while adotar not in ("n", "s"):
        adotar = input(
            "Saindo da câmara, você encontra um pato preso.\nDeseja adotá-lo? (S/N) "
        ).lower()
    if adotar == "s":
        pato_pet.ativo = True
        pato_pet.novo_nome()
        input(f"{pato_pet.nome} aumentou sua {pato_pet.qualidade} em {pato_pet.valor}")
        prota.vida += pato_pet.valor
        prota.companheiro = True
    elif adotar == "n":
        input("Você matou o pato.")
        input("Comendo ele você ganhou mais dano.")
        prota.companheiro = False
        prota.dano_min = prota.dano_min + 10
        prota.dano_max = prota.dano_max + 10
        prota.dano = f"{prota.dano_min} - {prota.dano_max}"
        prota.recalcular_status(prota.vida)
