import tkinter
from tkinter import Button, Entry, Label, PhotoImage
from modulos import imc

def acao():
    print("Botão pressionado!")
    #indice = imc.calcula_imc(peso=peso.get(),)

principal = tkinter.Tk()
# Código da interface aqui .
principal.geometry("250x150")

# Logo
imagem = PhotoImage(file="logo.png")
logo_label = Label(principal, image=imagem)
# Posiciona no topo-esquerda
logo_label.place(x=10, y=20)

#logo_label.image = imagem
logo_label.grid(row=0, column=0, rowspan=2)

# Etiqueta da Altura
label_altura = Label(principal, text="Altura: ")
label_altura.place(x=90, y=20) # Alinhado com o topo do ícone
#etiqueta_altura.grid(row=0, column=1)

# Caixa de entrada da Altura
altura = Entry(principal, width=8)
altura.place(x=165, y=20)
#altura.grid(row=0, column=2)

# Etiqueta do Peso
label_peso = Label(principal, text="Peso (kg): ")
label_peso.place(x=90, y=50) # Um pouco abaixo da altura

# Caixa de entrada do Peso
peso = Entry(principal, width=8)
peso.place(x=165, y=50)
#peso.grid(row=1, column=2)

#Botão para calcular
botao = Button(principal, text="Calcular", command=acao, fg="white", bg="#3498db")
botao.place(x=100, y=100) # Centralizado horizontalmente
#botao = Button(principal, text="Calcular", command=acao)
#botao.grid(row=2, column=2)

principal.mainloop()

