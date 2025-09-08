'''Arquivo para a criação dos animais'''
class Animal:
    '''Class base para animais.
    
    Inputs:
    - Nome: Nome do animal;
    - Vida: Quantidade de vida do animal;
    - Qualidade: O atributo que o animal altera no jogador:
    - Valor: Quantidade do atributo que o animal altera.'''
    def __init__(self, nome:str, vida:int, qualidade:str, valor:int, ativo:bool):
        self.nome = nome
        self.vida = vida
        self.qualidade = qualidade
        self.valor = valor
        self.ativo = ativo

    def __str__(self):
        return f"{self.nome}"

class Pato(Animal):
    '''Class para criar o pato'''
    def __init__(self):
        super().__init__("nome", 80, "vida", 20, False)

    def __str__(self):
        return f"{self.nome}"

    def novo_nome(self):
        '''Método para gerar o novo nome do pato.'''
        escolha = input("Deseja dar um nome para o pato: (S/N) ").lower()
        if escolha == 's':
            novo_nome = input("Digite o novo nome do pato: ")
            self.nome = novo_nome
        else:
            input("Ok, o pato se chamará Pato")
            self.nome = "Pato"