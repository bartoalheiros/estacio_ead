def calcula_imc(peso, altura):
    imc = float(peso) / float(altura) ** 2
    return imc

def classifica_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso adequado(normal)"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade Grau I"
    elif imc < 40:
        return "Obesidade Grau II(severa)"
    else:
        return "Obesidade Grau III(mórbida)"

if __name__ == '__main__':
    print(calcula_imc(70, 1.8))