'''
MIN E MAX

# Lista
lista = [1, 5, 3, 2, 6, 4, 9, 8]
print(max(lista))

# Tupla
tupla = 1, 5, 3, 2, 6, 4, 9, 8
print(max(tupla))

# Set
conjunto = {1, 5, 3, 2, 6, 4, 9, 8}
print(max(conjunto))

# Dicionario - Retorna chave
dicionario = {'a': 1, 'b': 5, 'c': 3, 'd': 2, 'e': 6, 'f': 4, 'g': 9, 'h': 8}
print(max(dicionario))

# Dicionario
dicionario = {'a': 1, 'b': 5, 'c': 3, 'd': 2, 'e': 6, 'f': 4, 'g': 9, 'h': 8}
print(max(dicionario.values()))

# Faça um programa que receba dois valores e retorne o maior

val1 = int(input('digite o primeiro valor: '))
val2 = int(input('digite o segundo valor'))

print(max(val1, val2))



print(max(1, 2, 3, 4, 6, 12, 7))
print(max('a', 'b', 'c'))
print(max('ana', 'carolina', 'aaaausmão'))

print(min(1, 2, 3, 4, 6, 12, 7))
print(min('a', 'b', 'c'))
print(min('ana', 'carolina', 'aaaausmão'))

nomes = ['ana', 'alamaster', 'cleiton', 'daniel', 'tim']

print(max(nomes))
print(min(nomes))

print(min(nomes, key=lambda nome: len(nome)))
print(max(nomes, key=lambda nome: len(nome)))

'''

musicas = [
    {'nome': 'La cucaracha', 'tocou': 3},
    {'nome': 'Mesopotamia', 'tocou': 10},
    {'nome': 'Manowar valley', 'tocou': 32},
    {'nome': 'Hino nacional', 'tocou': 47}
]

# print(min(musicas, key=lambda musica: musica['tocou']))

# print(max(musicas, key=lambda musica: musica['tocou'])['nome'])

print(max([musica['tocou'] for musica in musicas]))
