class Item:
    '''Class base para os equipamentos.'''
    def __init__(self, nome, descricao, tipo, ativo = False):
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome}'
    
class Arma(Item):
    '''Class para equipamento que muda o valor de ataque.'''
    def __init__(self, nome, descricao, dano_min, dano_max, tipo = "Arma", ativo=False):
        self.dano_min = dano_min
        self.dano_max = dano_max
        super().__init__(nome, descricao, tipo, ativo)

class Acessorio(Item):
    '''Class para equipamento que aumentam algum atributo.'''
    def __init__(self, nome, descricao, beneficio, tipo = "Acessório", ativo=False):
        self.beneficio = beneficio
        super().__init__(nome, descricao, tipo, ativo)

class Magico(Item):
    ''' Class para equipamento que liberam magias.'''
    def __init__(self, nome, descricao, tipo_magia, poder, ativo=False):
        self.tipo_magia = tipo_magia
        self.poder = poder   
        super().__init__(nome, descricao, ativo)
    
class Pocao(Item):
    "Class para poções."
    def __init__(self, nome, descricao, ativo=False):
        super().__init__(nome, descricao, ativo)