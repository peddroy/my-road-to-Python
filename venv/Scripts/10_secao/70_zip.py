'''

zip()

cria um iterável chamado zip object, 
que agrega elemento de cada um dos iteraveis passados como entrada em pares

sempre podemos retornar uma lista, tupla, set ou dicionário


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

print(list(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2, lista3) 
# o zip utiliza como parametro o menor tamanho em iterável,
# isso significa que se estiver trabalhando com iteráveis de tamanhos diferentes,
# irá parar quando os elemetos do menor iterável acabar

print(list(zip1))

# Podemos utilizar diferentes iteráveis como zip

tupla = 1, 2, 3, 4, 5
lista = [10, 11, 12, 13, 14]
conjunto = {'a', 'b', 'c', 'd', 'e'}
dicionario = {'w': 10, 'x': 100, 'y': '200', 'z': 200}
print(conjunto)

zip2 = zip(tupla, lista, conjunto, dicionario.values())

print(list(zip2))

# lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*dados)))

'''
# Exemplo mais complexo
# Retornar a nota mais alta do aluno

prova1 = [2, 5, 7]
prova2 = [6, 2, 8]
alunos = ['maria', 'pedro', 'marlon']

# final = {dado[0]: max(dado[1], dado[2])
#          for dado in zip(alunos, prova1, prova2)
#          }

# print(final)

# Podemos resolver com map

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))
