def calcula_imc(peso, altura):
    print("Parâmetro peso:", peso)
    print(f'Parâmetro altura: {altura:.2f}')
    imc = peso / (altura ** 2)
    print("IMC:",imc)

# Início do Programa
print("Início do programa")
calcula_imc(altura=1.80,peso=96)
print("Término do programa")
