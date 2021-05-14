from functools import reduce

'''
pessoas = [
    {'nome': 'Claudio', 'idade': 32, 'cores': ['azul', 'branca']},
    {'nome': 'Ademar', 'idade': 12, 'cores': ['amarelo', 'mentecapto']},
    {'nome': 'Oliveira', 'idade': 45, 'cores': ['verde', 'hardocre']},
    {'nome': 'Santos', 'idade': 103, 'cores': ['rouxa', 'alfazema']},
    {'nome': 'Luxa', 'idade': 63, 'cores': ['ciano', 'mertiolate']}
]


exmap = list(map(lambda pessoa: {**pessoa}, pessoas))

print(exmap)

#pegando um valor dentro de uma lista que esta dentro de uma biblioteca que esta dentro de uma lista
exmap[0]['cores'][0] = 'numismatica'

print(exmap)
# pegar


'''

produtos = [
    {'nome': 'P1', 'preco': 59.60, 'peso': 1.350, 'variacoes': ['a', 'b']},
    {'nome': 'P2', 'preco': 69.60, 'peso': 2.250, 'variacoes': ['c', 'd']},
    {'nome': 'P3', 'preco': 79.60, 'peso': 3.150, 'variacoes': ['e', 'f']},
    {'nome': 'P4', 'preco': 89.60, 'peso': 4.050, 'variacoes': ['g', 'h']},
    {'nome': 'P5', 'preco': 99.60, 'peso': 5.950, 'variacoes': ['i', 'j']},
    {'nome': 'P6', 'preco': 09.60, 'peso': 6.850, 'variacoes': ['k', 'l']}
]

# # Exemplo usando for padrão
# total_soma = 0
# for i in produtos:
#     total_soma = total_soma + i['preco']
# print(total_soma)
#
#
# # Exemplo passando uma função no reduce()
#
# def preco_reducer(soma, p):
#     return soma + p['preco']
#
# preco_total = reduce(preco_reducer, produtos, 0)
#
# print(preco_total)
#
#
# # Exemplo usando lambda no reduce
#
# preco_total = reduce(lambda soma, p: soma + p['preco'], produtos, 0)
#
# print(preco_total)


# Exemplo usando list comprehension

preco_total = sum([preco['preco'] for preco in produtos])

print(preco_total)


usuarios = [
    {'nome': 'Gomides', 'isactive': 1},
    {'nome': 'Salamandra' , 'isactive': 0} ,
    {'nome': 'Gusmão' , 'isactive': 1} ,
    {'nome': 'Sampaio' , 'isactive': 0} ,
    {'nome': 'Jeff' , 'isactive': 1} ,
]

ativos = map(lambda nome: nome['nome'], filter(lambda ativo: ativo['isactive'] == 1, usuarios))

print(list(ativos))