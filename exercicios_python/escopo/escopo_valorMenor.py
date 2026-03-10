def multiplicar():
    multiplicador = 3 # Variável local da função multiplicar
    print("Resultado da multiplicação:", valor * multiplicador)


valor = 10 # Variável global
multiplicar()
print("Variável [valor]", valor)
while True:
    if valor < 1000:
        print('Valor menor que 1000:', valor)
        break