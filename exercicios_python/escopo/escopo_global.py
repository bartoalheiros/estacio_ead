valor = 10

def multiplicar(numero):
    while numero < 100:
        if numero > valor:
            break
        numero *= 2
    return numero

print(multiplicar(3)) # Acessa a variável global "valor"