import tkinter as tk

janela = tk.Tk()

janela.title("Minha Aplicação")
janela.geometry("300x200")

# Criando um botão
botao = tk.Button(janela, text="Clique Aqui") #Posicionando
botao.place(x=50, y=50)

janela.mainloop()