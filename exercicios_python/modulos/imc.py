def calcula_imc(peso, altura):
    imc = float(peso) / float(altura) ** 2
    return imc
#calcula o peso ideal de uma pessoa, tendo como base o imc, calculado pela funcao calcula_imc
def calcula_peso_min_max(altura):
    altura_ao_quadrado = float(altura) * float(altura)
    peso_minimo = 18.5 * altura_ao_quadrado
    peso_minimo_uma_casa = round(peso_minimo, 1)
    peso_maximo = 24.9 * altura_ao_quadrado
    peso_maximo_uma_casa = round(peso_maximo, 1)
    return peso_minimo_uma_casa, peso_maximo_uma_casa

def classifica_imc(imc, altura):
    if imc < 18.5:
        min_val, max_val = calcula_peso_min_max(altura)
        peso_minimo = str(min_val)
        peso_maximo = str(max_val)
        return "Abaixo do peso. \nSeu peso ideal é entre: "  + peso_minimo + " e " + peso_maximo + "\nProcure um profissional."
    elif imc < 25:
        return "Peso adequado(normal)."
    elif imc < 30:
        min_val, max_val = calcula_peso_min_max(altura)
        peso_minimo = str(min_val)
        peso_maximo = str(max_val)
        return "Sobrepeso. \nSeu peso ideal é entre: "  + peso_minimo + " e " + peso_maximo + "\nProcure um profissional."
    elif imc < 35:
        min_val, max_val = calcula_peso_min_max(altura)
        peso_minimo = str(min_val)
        peso_maximo = str(max_val)
        return "Obesidade Grau I. \nSeu peso ideal é entre: "  + peso_minimo + " e " + peso_maximo + "\nProcure um profissional."
    elif imc < 40:
        min_val, max_val = calcula_peso_min_max(altura)
        peso_minimo = str(min_val)
        peso_maximo = str(max_val)
        return "Obesidade Grau II(severa). \nSeu peso ideal é entre: "  + peso_minimo + " e " + peso_maximo + "\nProcure um profissional."
    else:
        min_val, max_val = calcula_peso_min_max(altura)
        peso_minimo = str(min_val)
        peso_maximo = str(max_val)
        return "Obesidade Grau III(mórbida). \nSeu peso ideal é entre: " + peso_minimo + " e " + peso_maximo + "\nProcure um profissional."

if __name__ == '__main__':
    print(calcula_imc(70, 1.8))