class Item:
    def __init__(self, nome, descricao, tipo, dano_min, dano_max, ativo = False):
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        self.dano_min = dano_min
        self.dano_max = dano_max
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome}'