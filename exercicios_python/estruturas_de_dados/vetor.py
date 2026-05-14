from numpy import array

notas_real = array([2, 5, 10, 20, 50, 100], dtype=int)

print(notas_real[1])

#altera um valor de uma matriz
#m - > matriz, val - > novo valor, ln - > linha, col - > coluna
def altera_matriz(m,val,ln,col):
    m[ln][col] = val
    return m

#definir matriz é como definimos o vetor, só que a matriz vai ter várias dimensões
cadeiras = array([['Português', 'Matemática', 'Química'], ['História', 'Geografia', 'Física']], dtype=str)

#imprime elementos da matriz
#print(cadeiras[0][0])
#print(cadeiras[1][0])

#alterando elemento da matriz
#cadeiras[1][0] = 'Cálculo'
#print(cadeiras[1][0])

m = altera_matriz(cadeiras,'Desenho',0,1)

for linha in cadeiras:
    for elemento in linha:
        print(elemento)