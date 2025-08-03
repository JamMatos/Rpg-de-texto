class Jogador:
    def __init__(self, nome = "Fulano", vida = 100, energia = 100, dano ="3 - 5", dano_min=3, dano_max=5):
        self._nome = nome
        self.vida = vida
        self.energia = energia
        self.dano = dano
        self.dano_min = dano_min
        self.dano_max = dano_max
        self.inventario = []

    def __str__(self):
        return f'{self._nome}'

    def equipar_item(self, item):
        self.inventario.append(item)
        item.ativo= True    