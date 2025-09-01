"""Arquivo para rodar os testes automatizados"""

from unittest.mock import patch, MagicMock  # pylint: disable=unused-import
import pytest  # pylint: disable=unused-import
from routers.niveis.primeiro_nivel import primeiro_nivel
from models.monstros import Zombie, Esqueleto, Fantasma, ReiCadaver
from models.jogador import Jogador
from models.item_catalogo import (
    itens_loja,
    itens,
    Arma,
    Acessorio,
    Equipamento,
    Pocao,
    Magico,
)
from models.animal_catalogo import pato


# -------------------- Testes Unitário --------------------
def test_criacao_jogador():
    """Função teste para verificar se o jogador foi criado corretamente."""
    prota = Jogador()

    assert isinstance(prota, Jogador)
    assert prota.vida > 0
    assert hasattr(prota, "nome")


@pytest.mark.parametrize("class_monstro", [Zombie, Esqueleto, Fantasma, ReiCadaver])
def test_criacao_monstros(class_monstro):
    """Função teste para verificar se os monstros são criados corretamente."""
    monstro = class_monstro()
    assert monstro
    assert hasattr(monstro, "vida")
    assert monstro.vida > 0


def test_criacao_animal():
    """Função teste para verificar se o pato foi criado corretamente."""
    assert pato
    assert pato.vida > 0
    assert hasattr(pato, "nome")

@pytest.mark.parametrize("classe, atributos", [
    (Arma, ["preco", "dano_min", "dano_max"]),
    (Magico, ["preco", "atributo", "custo"]),
    (Pocao, ["preco", "atributo", "valor", "alvo"]),
    (Acessorio, ["preco", "valor", "atributo"]),
    (Equipamento, ["preco", "valor", "atributo"]),
])
@pytest.mark.parametrize("inventario", [itens, itens_loja])
def test_criacao_itens(classe, atributos, inventario):
    """Função teste para verificar se os itens foram criados corretamente."""
    assert "espada_madeira" in itens
    assert "peitoral_ferro" in itens_loja
    assert "peitoral_malha" not in itens_loja

    for nome, item in inventario.items():
        if isinstance(item, classe):
            for attr in atributos:
                assert hasattr(item, attr), f"{nome} deveria ter {attr}"

    # for nome, item in itens_loja.items():
    #     if isinstance(item, Arma):
    #         assert hasattr(item, "preco")
    #         assert hasattr(item, "dano_min")
    #         assert hasattr(item, "dano_max")
    #     elif isinstance(item, Magico):
    #         assert hasattr(item, "preco")
    #         assert hasattr(item, "atributo")
    #     elif isinstance(item, Pocao):
    #         assert hasattr(item, "preco")
    #         assert hasattr(item, "atributo")
    #         assert hasattr(item, "valor")
    #         assert hasattr(item, "alvo")
    #     elif isinstance(item, Acessorio):
    #         assert hasattr(item, "preco")
    #         assert hasattr(item, "atributo")
    #         assert hasattr(item, "valor")
    #     elif isinstance(item, Equipamento):
    #         assert hasattr(item, "preco")
    #         assert hasattr(item, "atributo")
    #         assert hasattr(item, "valor")

# -------------------- Testes Integração --------------------
def test_conectar_itens_ao_prota():
    """
    Função teste para verificar se os itens são conectados corretamente ao inventário do jogador.
    """
    prota = Jogador()
    # Verificar se a espada de madeira é adicionada perfeitamente
    prota.armazenar_item(itens["espada_madeira"])
    assert itens["espada_madeira"] in prota.inventario

    # Verificar se não aceita duplicação de itens
    prota.armazenar_item(itens["espada_madeira"])
    assert prota.inventario.count(itens["espada_madeira"]) == 1

    # prota.armazenar_item(itens_loja["peitoral_ferro"])
    # assert itens["peitoral_ferro"] in prota.inventario

# -------------------- Testes de Sistema --------------------

# -------------------- Testes de Integridade de Dados --------------------


# -------------------- Testes Usabilidade --------------------



class TesteProta:
    """Class que gerar um prota temporário para testes."""

    def __init__(self, vida):
        self.vida = vida


def test_primeiro_nivel_prota_morre():
    """Função para verificar se o prota morre corretamente no nível 1."""
    prota = Jogador()
    #inimigo = Zombie()

    with patch("routers.niveis.primeiro_nivel.Zombie") as mock_zombie, patch(
        "routers.niveis.primeiro_nivel.interface_batalha"
    ), patch("routers.niveis.primeiro_nivel.controles"), patch(
        "routers.niveis.primeiro_nivel.zerou_vida"
    ) as test_zerou:

        test_zombie = mock_zombie.return_value
        test_zombie.vida = 10

        prota.vida = 0

        nivel = primeiro_nivel(prota, nivel=1)

        assert nivel == 0
        test_zerou.assert_called_once()


def test_primeiro_nivel_prota_vence():
    """Função para verificar se o prota vencer corretamente o nível 1."""
    prota = Jogador()

    with patch("routers.niveis.primeiro_nivel.Zombie") as mock_zombie, patch(
        "routers.niveis.primeiro_nivel.interface_batalha"
    ), patch("routers.niveis.primeiro_nivel.zerou_vida"), patch(
        "routers.niveis.primeiro_nivel.controles"
    ) as test_controles:

        test_zombie = mock_zombie.return_value
        test_zombie.vida = 0  # inimigo derrotado
        prota.vida = 100
        test_controles.return_value = 2  # novo nível

        nivel = primeiro_nivel(prota, nivel=1)

        assert nivel == 2
