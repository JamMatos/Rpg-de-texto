class Monstro:
    def __init__(self, nome, vida, dano, dano_min, dano_max):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.dano_min = dano_min
        self.dano_max = dano_max

    def __str__(self):
        return f'{self.nome}'
    
class Esqueleto(Monstro):
    def __init__(self, nome = "Esqueleto", vida = 60, dano = "12 - 17", dano_min = 12, dano_max = 17):
        super().__init__(nome, vida, dano, dano_min, dano_max)

    def __str__(self):
        return super().__str__()
    
class Zombie(Monstro):
    def __init__(self, nome = "Zombie", vida = 75, dano = "9 - 14", dano_min = 9, dano_max = 14):
        super().__init__(nome, vida, dano, dano_min, dano_max)

    def __str__(self):
        return super().__str__()
    
class Fantasma(Monstro):
    def __init__(self, nome = "Fantasma", vida = 120, dano = "18 - 25", dano_min = 18, dano_max = 25):
        super().__init__(nome, vida, dano, dano_min, dano_max)

    def __str__(self):
        return super().__str__()