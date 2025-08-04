class Jogador:
    '''Class do personagem jogavel principal.'''
    def __init__(self, nome: str = "Fulano", vida:int = 100, energia:int = 100, dano:str = f"3 - 5", dano_min:int = 3, dano_max:int = 5, defesa:int = 0):
        self._nome = nome
        self.vida = vida
        self.energia = energia
        self.dano = dano
        self.dano_min = dano_min
        self.dano_max = dano_max
        self.defesa = defesa
        self.inventario = []

        # Valores base
        self.dano_base_min = 5
        self.dano_base_max = 15
        self.defesa_base = 0

    def __str__(self):
        return f'{self._nome}'

    def armazenar_item(self, item):
        '''Método que armazenar o equipamento para o jogador.'''
        self.inventario.append(item)
        item.ativo = True
        if item.tipo == "Arma":
            self.dano_min += item.dano_min
            self.dano_max += item.dano_max
            self.dano = f"{self.dano_min} - {self.dano_max}" 