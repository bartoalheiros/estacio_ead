# armazena o número de empréstimos feitos por dia da semana
numEmprestimos = [3,0,1,2,7,5,3]
somaL = 0
maior = 0
indiceDia = 0

for dia in range(1,8):
     somaL += numEmprestimos[dia-1]
     # guarda o maior valor da lista
     if maior < numEmprestimos[dia-1]:
         maior = numEmprestimos[dia-1]
         indiceDia = dia

print(f'A soma dos livros vendidos na semana é: {somaL}')
print(f'A média de livros vendidos na semana é: {somaL/7}')

if(indiceDia == 1):
    print(f'O dia com maior número de empréstimos foi Domingo')
elif(indiceDia == 2):
    print(f'O dia com maior número de empréstimos foi Segunda')
elif(indiceDia == 3):
    print(f'O dia com maior número de empréstimos foi Terça')
elif(indiceDia == 4):
    print(f'O dia com maior número de empréstimos foi Quarta')
elif(indiceDia == 5):
    print(f'O dia com maior número de empréstimos foi Quinta')
elif(indiceDia == 6):
    print(f'O dia com maior número de empréstimos foi Sexta')
elif(indiceDia == 7):
    print(f'O dia com maior número de empréstimos foi Sábado')



