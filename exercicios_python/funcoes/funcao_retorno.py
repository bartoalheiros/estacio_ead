def calcula_imc(peso,altura):
    return peso/(altura**2)

def main():
    indice = calcula_imc(96,1.80)
    print('Calculadora de IMC')
    print(f'IMC: {indice:.2f}')

    if indice < 18.5:
        print('Classificação: Abaixo do peso')
    elif indice < 25:
        print('Classificação: Peso ideal')
    elif indice < 30:
        print('Classificação: Sobrepeso')
    else:
        print('Classificação: Obesidade')

    print('\nTérmino do programa')

if __name__ == '__main__':
    main()