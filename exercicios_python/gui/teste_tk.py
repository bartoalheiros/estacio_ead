#import tkinter as tk
from tkinter import Tk, Button

def acao():
    print("Botão pressionado!")

principal = Tk()

# Criando um botão
botao = Button(principal, text="Clique Aqui", command=acao) #Posicionando
botao.place(x=100, y=25)

principal.mainloop()