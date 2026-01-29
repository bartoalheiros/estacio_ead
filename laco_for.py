numero = eval(input('Entre com um inteiro positivo: '))

for x in range(1,numero+1):
    if numero%x == 0:
        print(f'{x} é divisor de {numero}')
    else:
        print(f'{x} NÃO é divisor de {numero}')