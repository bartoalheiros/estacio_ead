import tkinter
from tkinter import Button, Entry, Label, PhotoImage, messagebox
from modulos import imc

def acao():
    indice = imc.calcula_imc(peso=peso.get(), altura=altura.get())
    classificacao = imc.classifica_imc(indice,altura.get())
    msg = messagebox.showinfo("Classifcação IMC", classificacao)

principal = tkinter.Tk()

# 1. Defina o tamanho da sua janela
largura_janela = 300
altura_janela = 150

# 2. Obtenha a largura e altura da tela do seu computador
largura_tela = principal.winfo_screenwidth()
altura_tela = principal.winfo_screenheight()

# 3. Calcule a posição X e Y para que a janela fique no meio
posicao_x = int((largura_tela / 2) - (largura_janela / 2))
posicao_y = int((altura_tela / 2) - (altura_janela / 2))

# 4. Configure a geometria com os valores calculados
# O formato é: "largura x altura + posiçãoX + posiçãoY"
principal.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

# Logo
try:
    imagem_original = PhotoImage(file="logo.png")

    # Reduz a imagem. Aumente esses números se ela ainda estiver grande.
    # Ex: subsample(4, 4) divide a largura e altura originais por 4.
    imagem_pequena = imagem_original.subsample(8, 8)

    logo_label = Label(principal, image=imagem_pequena)
    logo_label.image = imagem_pequena  # Mantém a referência ativa

    # row=0, column=0 coloca na primeira célula.
    # sticky="nw" garante que ela encoste no topo (North) e na esquerda (West).
    # padx e pady adicionam um pequeno respiro das bordas da janela.
    logo_label.grid(row=0, column=0, rowspan=2, sticky="nw", padx=5, pady=5)

except Exception as e:
    print(f"Erro ao carregar imagem: {e}")
    logo_label = Label(principal, text="LOGO", bg="gray")
    logo_label.grid(row=0, column=0, rowspan=2, sticky="nw", padx=5, pady=5)

# Posiciona no topo-esquerda
logo_label.place(x=10, y=20)

#logo_label.image = imagem
logo_label.grid(row=0, column=0, rowspan=2)

# Etiqueta da Altura
label_altura = Label(principal, text="Altura: ")
label_altura.place(x=135, y=20) # Alinhado com o topo do ícone
#etiqueta_altura.grid(row=0, column=1)

# Caixa de entrada da Altura
altura = Entry(principal, width=13)
altura.place(x=192, y=20)
#altura.grid(row=0, column=2)

# Etiqueta do Peso
label_peso = Label(principal, text="Peso (kg): ")
label_peso.place(x=135, y=50) # Um pouco abaixo da altura

# Caixa de entrada do Peso
peso = Entry(principal, width=13)
peso.place(x=192, y=50)
#peso.grid(row=1, column=2)

#Botão para calcular
botao = Button(principal, text="Calcular", command=acao, fg="white", bg="#3498db")
botao.place(x=175, y=100) # Centralizado horizontalmente
#botao = Button(principal, text="Calcular", command=acao)
#botao.grid(row=2, column=2)

# Vincula o Enter da janela à função acao
principal.bind('<Return>', lambda event: acao())
principal.mainloop()

