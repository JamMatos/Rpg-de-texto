class Monstro:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano

    def __str__(self):
        return f'{self.nome}'
    
class Esqueleto(Monstro):
    def __init__(self, nome = "Esqueleto", vida = 80, dano = 17):
        super().__init__(nome, vida, dano)

    def __str__(self):
        return super().__str__()
    
class Zombie(Monstro):
    def __init__(self, nome = "Zombie", vida = 90, dano = "9 - 14"):
        super().__init__(nome, vida, dano)

    def __str__(self):
        return super().__str__()