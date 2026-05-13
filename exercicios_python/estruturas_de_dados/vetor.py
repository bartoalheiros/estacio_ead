from numpy import array

notas_real = array([2, 5, 10, 20, 50, 100], dtype=int)

print(notas_real[1])

#definir matriz é como definimos o vetor, só que a matriz vai ter várias dimensões
cadeiras = array([['Português', 'Matemática', 'Química'], ['História', 'Geografia', 'Física']], dtype=str)

print(cadeiras[0][0])
print(cadeiras[1][0])