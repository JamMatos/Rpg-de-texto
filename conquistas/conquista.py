'''Arquivo para gerar o JSON das conquistas'''
import os
import json

CAMINHO_CONQUISTAS = "conquistas/conquistas.json"

# Conquistas iniciais zeradas
conquistas_iniciais = {
    "primeira_morte": False,
    "salvou_irmao": False
}

# Criar o arquivo caso não exista
if not os.path.exists(CAMINHO_CONQUISTAS):
    with open(CAMINHO_CONQUISTAS, "w", encoding="utf-8") as f:
        json.dump(conquistas_iniciais, f, indent=4, ensure_ascii=False)
    #print("Arquivo de conquistas criado.")

# Carregar as conquistas
with open(CAMINHO_CONQUISTAS, "r", encoding="utf-8") as f:
    conquistas = json.load(f)
