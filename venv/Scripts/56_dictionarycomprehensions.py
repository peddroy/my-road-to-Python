'''
DICTIONARY COMPREHENSIONS

Crior list

lista = [1, 2, 3, 4, 5]

Criar tuple

tupla = (1, 2, 3, 4, 5)  # or tupla = 1, 2, 3, 4, 5

Criar set (conjunto)

conjunto = {1, 2, 3, 4, 5}

Criar dictionary

dicionario = {'a': 1,'b': 2,'c': 3, 'd': 4, 'e': 5}

{chave: valor for valor in iteravel}

numeros = {'a': 1,'b': 2,'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

lista = [1, 2, 3, 4, 5]  #funciona com lista, tupla e set
quadrados = {valor: valor ** 2 for valor in lista}  # Criando um dict a partir de lista
print(quadrados)

# Se numero duplicado quando crio o dicionario ele não gera duplicado

'''

chaves = 'abcde'
numeros = [1, 2, 3, 4, 5]

mistura = {chaves[i]: numeros[i] for i in range(len(chaves))}
print(mistura)

res = {num: 'par' if num % 2 == 0 else 'impar' for num in numeros}
print(res)


pares = [2, 4, 6]
impares = [1, 3, 5]

mistura = [pares[i] or impares[i] for i in range(len(pares))]

print(mistura)
