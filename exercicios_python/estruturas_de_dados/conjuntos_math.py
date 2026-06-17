conjunto_a = {1, 2, 3}
conjunto_b = {4, 5, 6}
conjunto_b = {3, 4, 5}

print(conjunto_a)
print(conjunto_b)

uniao = conjunto_a.union(conjunto_b)
print(uniao)

intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)

#(a - b)
diferenca = conjunto_a.difference(conjunto_b)
print(diferenca)

#(b - a)
diferenca_2 = conjunto_b.difference(conjunto_a)
print(diferenca_2)