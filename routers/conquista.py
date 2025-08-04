'''Arquivo para gerar o JSON das conquistas'''
import json

conquistas = {
    "primeira_morte": False,
    "salvou_irmao": False,
}

with open('../conquistas.json', 'w', encoding="utf-8") as f:
    json.dump(conquistas, f, indent=4)
