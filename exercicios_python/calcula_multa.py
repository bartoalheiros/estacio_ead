multa = 0
print('====== Calculadora de Multa ======')
dias_atraso = int(input('Entre com o número de dias em atraso: '))

if(dias_atraso <= 3):
    multa = dias_atraso * 0.50
elif(dias_atraso > 3 
     and dias_atraso < 8):
    multa = dias_atraso * 1.00
elif(dias_atraso > 7):
    multa = dias_atraso * 2.00

print(f'O valor da multa é R$ {multa:.2f}')