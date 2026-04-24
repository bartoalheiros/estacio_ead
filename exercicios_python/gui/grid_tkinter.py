import tkinter
from tkinter import Button
from tkinter import Entry
from tkinter import Label

def acao():
    print('Botão Pressionado!')

principal = tkinter.Tk()
botao = Button(principal, text="Olá", command=acao)
botao.grid(row=0, column=2)

texto = Entry(principal) # coloca a caixa de texto na janela principal criada
texto.grid(row=0, column=1)

etiqueta = Label(principal, text="Label")
etiqueta.grid(row=0, column=0)

principal.mainloop()