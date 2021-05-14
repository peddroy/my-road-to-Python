'''

MODO - COLLECTIONS - NAMED TUPLE

https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recap Tupla

tupla = (1, 2, 3)

print(tupla[1])

Named Tupla - São tuplas diferenciadas onde especificamos um nome e parametros

# Realizar importação

from collections import namedtuple

# precisamos definir um nome e parametros

# forma 1 - declaração named tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

#forma 2 - declaração named tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - declaração named tuple - preferivel

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#usando a named tuple

ray = cachorro(idade=2, raca='pitbull', nome='Ray')

# Acessando os dados
# Forma 1

print(ray)

print(ray[0]) #idade
print(ray[1]) #raça
print(ray[2]) #nome

# Forma 2
print(ray.idade)
print(ray.raca)
print(ray.nome)


# Qual o indice?
print(ray.index('pitbull'))

# Quantas ocorrencias?
print(ray.count('pitbull'))


'''

