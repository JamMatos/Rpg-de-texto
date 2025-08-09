'''Arquivo com as class das criaturas'''
class Monstro:
    '''Class base para os monstros'''
    def __init__(self, nome, vida, dano, dano_min, dano_max):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.dano_min = dano_min
        self.dano_max = dano_max

    def __str__(self):
        return f'{self.nome}'

class Esqueleto(Monstro):
    '''Class que definir a criatura Esqueleto'''
    def __init__(self, nome = "Esqueleto", vida = 60, dano = "12 - 17",
        dano_min = 12, dano_max = 17):
        super().__init__(nome, vida, dano, dano_min, dano_max)


class Zombie(Monstro):
    '''Class que definir a criatura Zombie'''
    def __init__(self, nome = "Zombie", vida = 75, dano = "5 - 11", dano_min = 5, dano_max = 11):
        super().__init__(nome, vida, dano, dano_min, dano_max)


class Fantasma(Monstro):
    '''Class que definir a criatura Fantasma'''
    def __init__(self, nome = "Fantasma", vida = 120, dano = "18 - 25",
        dano_min = 18, dano_max = 25):
        super().__init__(nome, vida, dano, dano_min, dano_max)

class ReiCadaver(Monstro):
    '''Class que definir a criatura Rei Cadáver.'''
    def __init__(self, nome = "Rei Cadáver", vida = 200, dano = "30 - 45",
    dano_min = 30, dano_max = 45):
        super().__init__(nome, vida, dano, dano_min, dano_max)
