"""Arquivo onde ficar os items para serem chamados."""

# import random
from models.item import Arma, Acessorio, Magico, Pocao

espada_madeira = Arma("Espada de Madeira", "Uma espada velha de madeira", 5, 10)
anel_rubi = Acessorio(
    nome = "Anel de Rubi",
    descricao = "Um anel prateado com um rubi no centro",
    valor = 6,
    atributo= "dano",
)
KingNote = Magico(
    "Anotações do Rei",
    "Um pequeno livro magenta",
    "O jogador invoca chamas de cor magenta em cima do inimigo",
    "Chamas magentas",
    50,
    25,
)
GoldRain = Magico(
    "Chuva Dourada",
    "Um livro amarelo com 3 lanças na capa",
    "Um ataque feito com lanças douradas saiem do teto atacado o inimigo ",
    "Ataque físico mágico",
    30,
    15,
)
espada_fantasma = Arma(
    "Ectosword", "Uma lámina prateada imbuido com ectoplasma", 12, 20
)
pocao_vida_p = Pocao(
    "Poção pequena de vida", 
    "Um frasco cilindrico com um liquido vermelho",
    "vida", 
    20,
    "Jogador",
    3)
