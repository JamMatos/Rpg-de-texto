class Jogador:
    def __init__(self, nome, vida, energia, dano, dano_min, dano_max):
        self._nome = nome
        self.vida = vida
        self.energia = energia
        self.dano = dano
        self.dano_min = dano_min
        self.dano_max = dano_max

    def __str__(self):
        return f'{self.nome}'
    