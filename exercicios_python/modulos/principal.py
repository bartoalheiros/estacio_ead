import imc as c
from imc import classifica_imc as c_imc

peso = 70
altura = 1.8

indice = c.calcula_imc(90, 1.5)
print(indice)
classifica_imc = c_imc(indice)
print(classifica_imc)