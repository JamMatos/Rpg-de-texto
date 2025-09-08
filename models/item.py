"""Arquivo para as class dos itens"""

from enum import Enum


class Alvo(Enum):
    """Class para delimitar os tipos de alvos que as poções podem ter."""

    JOGADOR = "Jogador"
    INIMIGO = "Inimigo"
    AMBOS = "Ambos"


class Item:
    """Class base para os equipamentos.

    Inputs:
    - Nome: Como o item é nomeado;
    - Descrição: Um breve texto detalhando ele;
    - Tipo: Determinação do grupo que pertence;
    - Ativo: Se o jogador pode utilizar dele."""

    def __init__(self, nome: str, descricao: str, tipo: str, preco:int, ativo: bool = False):
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        self.ativo = ativo
        self.preco = preco

    def to_dict(self):
        '''Função para ter os dados em json'''
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "tipo": self.tipo,
            "ativo": self.ativo,
            "preco": self.preco
        }


class Arma(Item):
    """Class para equipamento que muda o valor de ataque.

    Inputs:
    - Dano Mínimo: Valor mínimo de dano que a arma pode causar;
    - Dano Máximo: Valor máximo de dano que a arma pode causar."""

    def __init__(
        self,
        nome: str,
        descricao: str,
        preco:int,
        dano_min: int,
        dano_max: int,
        ativo: bool = False,
    ):
        self.dano_min = dano_min
        self.dano_max = dano_max
        super().__init__(nome, descricao, "Arma", preco, ativo)

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "dano_min": self.dano_min,
            "dano_max": self.dano_max
        })
        return base

class Acessorio(Item):
    """Class para equipamento que aumentam algum atributo.

    Inputs:
    - Valor: Quantidade do atributo que o acessório produz."""

    def __init__(self, nome, descricao, valor, atributo,preco, ativo=False):
        self.valor = valor
        self.atributo = atributo
        super().__init__(nome, descricao, "Acessório", preco, ativo)

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "valor": self.valor,
            "atributo": self.atributo
        })
        return base


class Magico(Item):
    """Class para equipamento que liberam magias.

    Inputs:
    - Descrição de ataque: narração do ataque feito com o item mágico;
    - Atributo: Qual efeito o item mágico produz;
    - Valor: Quantidade do atributo que o item mágico produz;
    - Custo: Quantidade de energia que gasta do usuário para ser usado."""

    def __init__(
        self,
        nome,
        descricao,
        descricao_ataque: str,
        atributo,
        valor,
        custo,
        preco,
        ativo=False,
    ):
        self.descricao_ataque = descricao_ataque
        self.atributo = atributo
        self.valor = valor
        self.custo = custo
        super().__init__(nome, descricao, "Mágico", preco, ativo)

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "descricao_ataque": self.descricao_ataque,
            "atributo": self.atributo,
            "valor": self.valor,
            "custo": self.custo
        })
        return base


class Pocao(Item):
    """Class para poções.

    Inputs:
    - Atributo: Qual efeito a poção produz;
    - Valor: Quantidade do atributo que a porção produz;
    - Alvo: Indicar em quem usar a poção;
    - Quantidade: Quantidade do item para adicionar ao jogador."""

    def __init__(self, nome: str, descricao: str, atributo: str, valor: int,
        preco:int, alvo: Alvo, quantidade: int, ativo=False):

        self.atributo = atributo  # Cura, dano, paralisia
        self.valor = valor  # Quantidade que dá do seu atributo
        self.alvo = alvo  # Indica em quem usar a poção
        self.quantidade = quantidade # Quantidade do item para adicionar ao jogador
        super().__init__(nome, descricao, "Poção", preco, ativo)

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "atributo": self.atributo,
            "valor": self.valor,
            "alvo": self.alvo,
            "quantidade": self.quantidade
        })
        return base

    def usar(self):
        '''Função que utiliza da poção até a quantidade chegar a 0.'''
        if self.quantidade > 0:
            self.quantidade -= 1
            return True
        return False

class Equipamento(Item):
    '''Class para equipamento, tipo armadura.
    
    Inputs:
    - Atributo: Qual efeito a poção produz;
    - Valor: Quantidade do atributo que a porção produz;
    - Local: Parte do corpo onde ficará a armadura;'''
    def __init__(self, nome, descricao, atributo, valor, preco, local, ativo = False):
        self.atributo = atributo  # Cura, dano, paralisia
        self.valor = valor  # Quantidade que dá do seu atributo
        self.local = local
        super().__init__(nome, descricao, "Armadura", preco, ativo)

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "atributo": self.atributo,
            "valor": self.valor,
        })
        return base

    def usar_defesa(self, prota):
        '''Método para calcular a defesa do jogador'''
        prota.defesa = self.valor
