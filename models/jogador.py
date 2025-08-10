"""Arquivo para a class do jogador"""
# from enum import Enum

# class Vida(Enum):
#     '''Class para criar uma viagem da vida'''

#     CHEIA = "♥"
#     VAZIO = "♡"

class Jogador:
    """Class do personagem jogavel principal."""
    def __init__(
        self,
        nome: str = "Fulano",
        vida: int = 100,
        energia: int = 100,
        dano_min: int = 3,
        dano_max: int = 5,
        defesa: int = 0,
    ):
        self.nome = nome
        self.vida = vida
        self.energia = energia
        self.dano = f"{dano_min} - {dano_max}"
        self.dano_min = dano_min
        self.dano_max = dano_max
        self.defesa = defesa
        self.inventario = []
        self.companheiro = True
        self.dinheiro = 0

        # Valores base
        self.dano_base_min = 3
        self.dano_base_max = 5
        self.defesa_base = 0
        #self.vida_base = vida

    def __str__(self):
        return f"{self.nome}"

    def armazenar_item(self, item):
        """Método que armazenar o equipamento para o jogador."""
        self.inventario.append(item)
        item.ativo = True
        if item.tipo == "Arma":
            self.dano_min += item.dano_min
            self.dano_max += item.dano_max
            self.dano = f"{self.dano_min} - {self.dano_max}"

    def recalcular_status(self):
        """Função que recalcular os dados do personagem."""
        # Reseta os valores
        if self.companheiro is False:
            self.dano_min = self.dano_base_min + 10
            self.dano_max = self.dano_base_max + 10
        else:
            self.dano_min = self.dano_base_min
            self.dano_max = self.dano_base_max
        self.defesa = self.defesa_base
        #self.vida = self.vida_base

        for item in self.inventario:
            if item.ativo and item.tipo == "Arma":
                self.dano_min += item.dano_min
                self.dano_max += item.dano_max
            elif item.ativo and item.tipo == "Acessório":
                if item.atributo == "defesa":
                    self.defesa += item.valor
                elif item.atributo == "vida":
                    self.vida += item.valor
                elif item.atributo == "dano":
                    self.dano_min += int(item.valor / 2)
                    self.dano_max += int(item.valor / 2)
            elif item.ativo and item.tipo == "Armadura":
                self.defesa += item.valor

        self.dano = f"{self.dano_min} - {self.dano_max}"
