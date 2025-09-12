"""Arquivo para testar GUI"""

import tkinter as tk
from tkinter import messagebox


texto = {
    1: "Você é um jovem fazendeiro cuidando das terras que antes foram dos seus pais, "
    "quando um grupo de monstros atacou \ne sequestraram seu irmão mais novo, Carlos, "
    "e agora você deve criar coragem e ir resgatá-lo.",
    2: "Ao entrar no covil dos monstros, você pega uma espada de madeira.",
    3: "Entrando na primeira câmara você se encontrar com seu primeiro inimigo, um Zumbi.",
    4: "Você encontrou um anel de rubi e uma roupa de malha."
    "Você encontrou alguns frascos pequenos com um líquido vermelho."
}

texto_especial = {
    1: "🎉 Conquista desbloqueada: Matou seu primeiro inimigo!"
}

def limpar_tela(janela):
    """Função que limpa a tela"""
    # Limpa janela antes de desenhar o mapa de novo
    for widget in janela.winfo_children():
        widget.destroy()

def fluxo(janela, num):
    """Função que chama os textos"""

    lable = tk.Label(janela, text=texto[num])
    lable.pack(pady=10)
    lable.config(bg="black", fg="white")

def registro():
    """Função para registrar o nome do jogador"""
    janela = tk.Tk()
    janela.title("Registro")
    janela.geometry("800x800")
    janela.config(bg="teal")

    lable = tk.Label(janela, text="Digite seu nome:")
    lable.pack(pady=5)
    lable.config(bg="orange")

    inptu = tk.Entry(janela, width=30)
    inptu.pack(pady=5)

    def entrar():
        """Chamar a matrix"""
        resposta = inptu.get()
        if resposta:
            janela.destroy()
            return resposta
        else:
            messagebox.showwarning(
                "Campo Obrigatório", "Por favor, preencha este campo."
            )
            # Opcional: Podes mudar a cor do campo para indicar erro
            inptu.config(bg="pink")

    botoa = tk.Button(janela, text="Ok", command=entrar)
    botoa.pack(pady=10)

    janela.mainloop()
