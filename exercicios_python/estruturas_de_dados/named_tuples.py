import collections

Pessoa = collections.namedtuple('Pessoa', 'nome idade')

joao = Pessoa(nome = 'João', idade = 20)
print(joao.nome)