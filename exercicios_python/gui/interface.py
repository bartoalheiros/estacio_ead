import tkinter
from tkinter import Button
from tkinter import Entry
from tkinter import Label

def acao():
    print("Botão pressionado!")

principal = tkinter.Tk()
# Código da interface aqui .

botao = Button(principal, text="Olá", command=acao) #Posicionando
botao.place(x=100, y=25)

principal.mainloop()

