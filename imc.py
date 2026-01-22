peso = eval(input('Entre com o seu peso: '))
altura = eval(input('Entre com a sua altura:'))
imc = peso/(altura**2)
print('IMC = ', imc)

if(imc < 18.5):
    print('Você está abaixo do peso.\n Procure o nutricionista para uma análise mais detalhada.')
elif(imc >= 18.5 and imc < 25):
    print('Seu peso está normal.\n Continue se cuidando.')
elif(imc >= 25 and imc < 30):
    print('Você possui Sobrepeso.\n Procure o nutricionista para uma análise mais detalhada.')
elif(imc >= 30 and imc < 35):
    print('Você possui Obesidade Grau I.\n Procure o nutricionista para uma análise mais detalhada.')
elif(imc >= 35 and imc < 40):
    print('Você possui Obesidade Grau II.\n Procure o nutricionista para uma análise mais detalhada.')
elif(imc >= 40):
    print('Você possui Obesidade Grau II.\n Procure o nutricionista para uma análise mais detalhada.')
