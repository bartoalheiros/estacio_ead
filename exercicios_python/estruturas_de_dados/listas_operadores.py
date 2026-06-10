lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = [4, 5, 6]

print(lista1 == lista2)
print(lista1 == lista3)

if 3 in lista1:
    print('Achei o 3!!!')

nova_lista = lista1 + lista3
print(nova_lista)

lista = [1, 2, 3]
nova_lista = [item*2 for item in lista]
print(nova_lista)

lista = [ 0, 1, 2, 3, 4, 5, 6]
nova_lista = [item for item in lista if item%2 == 0]
print(nova_lista)