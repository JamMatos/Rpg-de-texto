"""Arquivo onde ficar os items para serem chamados."""

# import random
from models.item import Arma, Acessorio, Magico, Pocao, Equipamento

espada_madeira = Arma(
    "Espada de Madeira", "Uma espada velha de madeira", 30, 7, 10
)

espada_fantasma = Arma(
    "Ectosword", "Uma lámina prateada imbuido com ectoplasma", 50, 12, 20
)

anel_rubi = Acessorio(
    nome="Anel de Rubi",
    descricao="Um anel prateado com um rubi no centro",
    preco=30,
    valor=8,
    atributo="dano",
)

king_note = Magico(
    "Anotações do Rei",
    "Um pequeno livro magenta",
    "O jogador invoca chamas de cor magenta em cima do inimigo",
    "Chamas magentas",
    50,
    25,
    40,
)

gold_rain = Magico(
    "Chuva Dourada",
    "Um livro amarelo com 3 lanças na capa",
    "Um ataque feito com lanças douradas saiem do teto atacado o inimigo ",
    "Ataque físico mágico",
    30,
    15,
    60,
)

pocao_vida_p = Pocao(
    "Poção pequena de vida",
    "Um frasco cilindrico com um liquido vermelho",
    "Vida",
    30,
    20,
    "Jogador",
    3,
)

pocao_vida_g = Pocao(
    "Poção grande de vida",
    "Um frasco cilindrico com um liquido vermelho",
    "Vida",
    60,
    40,
    "Jogador",
    5,
)

pocao_energia = Pocao(
    "Poção de energia",
    "Um frasco quadrado com um líquido verde",
    "Energia",
    30,
    30,
    "Jogador",
    3,
)

peitoral_malha = Equipamento(
    "Peitoral de malha", "Um armadura para o peito feito de malha", "Defesa", 6, 20
)

itens = {
    "espada_madeira": espada_madeira,
    "espada_fantasma": espada_fantasma,
    "anel_rubi": anel_rubi,
    "king_note": king_note,
    "gold_rain": gold_rain,
    "pocao_vida_p": pocao_vida_p,
    "pocao_vida_g": pocao_vida_g,
    "pocao_energia": pocao_energia,
    "peitoral_malha": peitoral_malha,
}

peitoral_ferro = Equipamento(
    "Peitoral de ferro", "Um peitoral feito de ferro", "Defesa", 12, 30
)

anel_safira = Acessorio(
    "Anel de safira", "Um anel de ouro branco com uma safira no meio", "vida", 20, 30
)

anel_esmeralda = Acessorio(
    "Anel de esmeralda",
    "Um anel de ouro amarelo com uma esmerala no meio",
    "energia",
    50,
    30,
)

por_do_sol = Magico(
    "Pôr do sol", "Um pequeno livro com uma capa de couro", "", "Uma luz", "80", 90, 50
)


itens_loja = {
    "peitoral_ferro": peitoral_ferro,
    "anel_safira": anel_safira,
    "anel_esmeralda": anel_esmeralda,
    "por_do_sol": por_do_sol,
}
