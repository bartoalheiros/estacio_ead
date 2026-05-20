from numpy import array

#altera um valor em uma matriz
#m - > matriz, val - > novo valor, ln - > linha, col - > coluna
def altera_matriz(m,val,ln,col):
    m[ln][col] = val
    return m

def imprime_matriz(m):
    # imprime a matriz completa
    for linha in m:
        print("\n")
        for elemento in linha:
            print(elemento)

#definir matriz é como definimos o vetor, só que a matriz vai ter várias dimensões
cadeiras = array([['Português', 'Matemática', 'Química'], ['História', 'Geografia', 'Física']], dtype=str)
imprime_matriz(cadeiras)

#alterando elemento da matriz
cadeiras[1][0] = 'Cálculo'

m = altera_matriz(cadeiras,'Desenho',0,1)

imprime_matriz(m)
