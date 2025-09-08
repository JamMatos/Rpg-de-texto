"""Arquivo onde ficar os items para serem chamados."""

# import random
from models.item import Arma, Acessorio, Magico, Pocao, Equipamento

# ----------------------------- Itens obtidos durante o jogo -----------------------------

espada_madeira = Arma("Espada de Madeira", "Uma espada velha de madeira", 30, 7, 10)

espada_fantasma = Arma(
    "Ectosword", "Uma lámina prateada imbuido com ectoplasma", 50, 15, 20
)

anel_rubi = Acessorio(
    nome="Anel de Rubi",
    descricao="Um anel prateado com um rubi no centro",
    preco=30,
    valor=8,
    atributo="dano",
)

pingente_do_macaco = Acessorio(
    nome="Pingente do Macaco",
    descricao="Um pigente dourado com um formato de um macaco",
    valor=20,
    atributo="dano",
    preco=0,
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
    "Peitoral de malha",
    "Um armadura para o peito feito de malha",
    "Defesa",
    6,
    20,
    "Peitoral",
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
    "pingente_do_macaco": pingente_do_macaco,
}

# ----------------------------- Itens da Loja -----------------------------

peitoral_ferro = Equipamento(
    "Peitoral de ferro", "Um peitoral feito de ferro", "Defesa", 12, 30, "Peitoral"
)

anel_safira = Acessorio(
    "Anel de safira", "Um anel de ouro branco com uma safira no meio", 20, "vida", 30
)

anel_esmeralda = Acessorio(
    "Anel de esmeralda",
    "Um anel de ouro amarelo com uma esmerala no meio",
    50,
    "energia",
    30,
)

espada_ferro = Arma(
    nome="Espada de Ferro",
    descricao="Uma espada de madeira de lei com lâmina de ferro",
    preco=30,
    dano_min=10,
    dano_max=15,
)

por_do_sol = Magico(
    "Pôr do sol",
    "Um pequeno livro com uma capa de couro",
    "Um belissimo e grandioso ataque de luz",
    "Uma luz",
    80,
    90,
    50,
)

saia_diva_em_dobro = Equipamento(
    "Saia Diva em Dobro",
    "Uma saia florida(Você se sente bonita?)",
    "Vida",
    80,
    50,
    "Calça",
)

itens_loja = {
    "peitoral_ferro": peitoral_ferro,
    "anel_safira": anel_safira,
    "anel_esmeralda": anel_esmeralda,
    "por_do_sol": por_do_sol,
    "saia_diva_em_dobro": saia_diva_em_dobro,
    "espada_ferro": espada_ferro,
}
