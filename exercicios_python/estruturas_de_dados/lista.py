#mostrando um item específico da lista
print('Mostrando a lista criada..')
lista = ['a', 'b', 'c', 'd']
print(lista)
print('Mostrando o segundo item da lista, de índice 1')
item = lista[1]
print(item)

# descobrindo o índice de um elemento na lista
# lista = ['a', 'b', 'c', 'b']
# indice_c = lista.index('c')
# print(indice_c)
#
# indice_b = lista.index('b')
# print(indice_b)

# lista = ['avião', 'helicóptero', 'carro', 'navio']
# indice_carro = lista.index('carro')
# print(indice_carro)

#Alteração do elemento na posição de índice 2 da lista
# lista[indice_carro] = 'moto'
# print(lista)

#percorrendo listas em python
#verificar porque não funciona.
#lista = ['a', 'b', 'c', 'd']
#for elemento in lista:
#    print(elemento)

# minha_lista = [1, 'moto', [1, 2, 3]]
# for elemento in minha_lista:
#    print(elemento)

#contando as posições da lista
# lista = ['a', 'b', 'c', 'd']
# for i in range(0, len(lista)):
#    print(i)

# lista = list()
# lista.append('carro')
# print(lista)
# lista.append('moto')
# lista.append('avião')
# print(lista)
# lista.insert(1, 'bicicleta') #insere o elemento bicicleta na posição de índice 1
# print(lista)

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_a.append(lista_b)
# print(lista_a)
#[1, 2, 3, [4, 5, 6]] lista_b foi adicionada dento da lista_a como um elemento único
# lista_a = [1, 2, 3]
# lista_a.extend(lista_b)
# print(lista_a)
#[1, 2, 3, 4, 5, 6] lista_a e lista_b foram concatenadas

#remove - remover elementos da lista
# lista = ['carro', 'bicicleta', 'moto', 'avião']
# lista.remove('bicicleta')
# print(lista)
# lista.clear()
# print(lista)

#ordenacao de elementos numa lista
#lista = [3, 2, 1, 6, 9]
#lista.sort() #ordena a lista de forma crescente
#print(lista)

#lista.reverse()#ordena os elementos da lista de forma decrescente
#print(lista)

#funcoes internas do Python
lista = [3, 7, 2, 6]
print('O comprimento da lista é: ') #tamanho da lista
print(len(lista))
print('O valor mínimo da lista é: ')
print(min(lista)) #elemento de valor mínimo
print('O valor máximo da lista é: ')
print(max(lista)) #elemento de valor máximo
print('A soma dos elementos da lista é: ')
print(sum(lista)) #soma de elementos da lista

lista = [1, 3, 5, 7, 9]