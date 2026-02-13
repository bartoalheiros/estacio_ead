#script selecao.py
def selecionador(seq, teste):
    selecionados = []

    for elemento in seq:
        if (teste(elemento)):
            selecionados.append(elemento)

    return selecionados

def verifica_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

def verifica_impar(num):
    if num % 2 == 0:
        return False
    else:
        return True

#parte principal do programa
def main():
    lista = [0, 1, 2, 3, 10]
    numeros_pares = selecionador(lista, verifica_impar)

    for num in numeros_pares:
        print(f" {num} -> impar")

if __name__ == "__main__":
    main()