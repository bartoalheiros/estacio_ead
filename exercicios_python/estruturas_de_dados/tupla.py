# tupla = ('a', 'b', 'c')
# item = tupla[2]
# print(item)
#
# indice_a = tupla.index('a')
# print(indice_a)

#imutabilidade - tuplas são imutáveis, logo
#se você tentar alterar qualquer elemento de uma, vai dar erro
# tupla = ('a', 'b', 'c')
# tupla[2] = 'd'

# tupla = ('a', 'b', [1, 2, 3], (1, 2, 3))
# for elemento in tupla:
#     print(elemento)

#dicionário: estrutura de dado com o formato 'chave: valor'
agenda = {('João', 'Silva'):'111222', ('Maria', 'Santos'): '3333444', ('Antonio', 'Souza'): '555666'}

print(agenda[('Antonio', 'Souza')])