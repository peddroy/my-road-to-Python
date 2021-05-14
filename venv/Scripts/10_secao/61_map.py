'''

MAP

com map fazemos mapeamento de valores para função
map é uma função que recebe dois parametros: o primeiro a função e o segundo um iteravel
mnap retorna um Object Map
Geralmento se passa uma expressão lambda no primeiro parametro


import math

def area(r):
    """Função que calcula a area de um circulo com raio 'r'"""
    return math.pi * (r ** 2)

print(f'{area(2):.2f}')
print(area(3))

# Modo padrão

raios = [2, 3, 4.5, 8, 12]

areas = []
for raio in raios:
    areas.append(area(raio))

print(f'{areas}')

# Utilizando map

area_map = map(area, raios)

print(area_map)
print(type(area_map))
print(list(area_map))

# Utilizando map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS. Após utilizar a função map() depois da primeira utilização do resultado ele zera (a lista fica vazia)
# ele se 'auto destroi' e limpa a memoria


# Para fixar:
#
# Temos dados iteraveis
# dados : a1, a2... an
#
# Temos uma função
# f(x)
#
# Utilizamos a função map(f, dados) onde o map ira mapear cada elemento dos dados e aplicar a função
#
# O retorno Object Map entrega o resultado da aplicação da função para cada dado

# Outro exemplo de aplicação

cidades = [('Berlin', 29), ('Tokyo', 18), ('New York', -4), ('Deli', 40),
           ('Curitiba', 19), ('Santos', 28), ('Manaus', 32)]

# f = 9/5 * c + 32

c_para_f = lambda cidades: (cidades[0], (9/5) * cidades[1] + 32)

print(list(map(c_para_f, cidades)))

print(c_para_f(cidades[2]))

# relembrando lambda

x = [1, 2, 3, 4]

teste = lambda x: (x + 5)

print(list(map(teste, x)))

# no map a função recebe apenas um parametro


# outro exercicio


kph = [52, 65, 76, 69, 80, 82, 87, 90, 95, 97, 110, 120]

print(list(map(lambda velocidade: (velocidade / 1.61), kph)))


'''
from pprint import pprint
print = pprint
pprint = print

produtos = [
    {'nome': 'P1', 'preço': 59.60, 'peso': 1.350, 'variações': ['a', 'b']},
    {'nome': 'P2', 'preço': 69.60, 'peso': 2.250, 'variações': ['c', 'd']},
    {'nome': 'P3', 'preço': 79.60, 'peso': 3.150, 'variações': ['e', 'f']},
    {'nome': 'P4', 'preço': 89.60, 'peso': 4.050, 'variações': ['g', 'h']},
    {'nome': 'P5', 'preço': 99.60, 'peso': 5.950, 'variações': ['i', 'j']},
    {'nome': 'P6', 'preço': 09.60, 'peso': 6.850, 'variações': ['k', 'l']}
]

# print(produtos)

# pegando preço com for
'''
produtos_map = []
for preço in produtos:
    produtos_map.append(preço['preço'])

print(produtos_map)
'''
# PEGANDO PREÇO COM LIST COMPREHENSION

produtos_listcomprehension = [round(produto['preço'] * 1.05) for produto in produtos]
print(produtos_listcomprehension)


'''
# INICIO // PEGANDO PREÇO COM MAP (ao final criar o dict novamente e altera o preço

# pegando o preço

produtos_map = list(map(lambda produto: produto['preço'], produtos))

print(f'1. Gerei uma lista que retorna o preço dos produtos')
print(produtos_map)


# arredonda preço

produtos_map = list(map(lambda produto: round(produto['preço']), produtos))

print(f'2. Arredondei o preço')
print(produtos_map)


# realiza calculo com o preço

produtos_map = list(map(lambda produto: round(produto['preço'] * 1.05), produtos))

print(f'3. realiza calculo com o preço')
print(produtos_map)


# recria biblioteca com chave preço e valor recalculado

produtos_map = list(map(lambda produto: {'preço': round(produto['preço'] * 1.05)}, produtos))

print(f'4. recria biblioteca')
print(produtos_map)


# faz unpacking de toda a biblioteca e substitui o preço original pelo calculado

produtos_map = list(map(lambda produto: {**produto, 'preço': round(produto['preço'] * 1.05)}, produtos))

print('5. faz unpacking e reconstroi a lista substituindo o valor')
print(produtos_map)


# TERMINO // PEGANDO PREÇO COM MAP (ao final criar o dict novamente e altera o preço


'''

produtos = [
    {'nome': 'P1', 'preço': 59.60, 'peso': 1.350, 'variações': ['a', 'b']},
    {'nome': 'P2', 'preço': 69.60, 'peso': 2.250, 'variações': ['c', 'd']},
    {'nome': 'P3', 'preço': 79.60, 'peso': 3.150, 'variações': ['e', 'f']},
    {'nome': 'P4', 'preço': 89.60, 'peso': 4.050, 'variações': ['g', 'h']},
    {'nome': 'P5', 'preço': 99.60, 'peso': 5.950, 'variações': ['i', 'j']},
    {'nome': 'P6', 'preço': 09.60, 'peso': 6.850, 'variações': ['k', 'l']}
]

ret = lambda x, y: x + y

total = reduce(ret, produtos)
