'''
SORTED

Apesar do nome não confundir sorted com sort().
sort() só funciona em listas

sorted() funciona com qualquer iterável

Como o nome diz ele serve para ordenar

O sorted() sempre retorna uma Lista


numeros = [1, 1, 1, 7, 4, 3, 8, 9, 2, 5]

print(sorted(numeros))  # ordena de forma crescente
print(set(sorted(numeros, reverse=True)))
    
'''
# import pprint
# print = pprint
# pprint = print

user = [
    {'username': 'samuel', 'tweets': ['amo chocolate', 'bora lá']},
    {'username': 'carlinhah2o', 'tweets': ['hoje ta legal', 'sei não']},
    {'username': 'xhiui', 'tweets': []},
    {'username': 'santosoficial', 'tweets': []},
    {'username': 'nasmateparamimepara', 'tweets': ['gratiluz']}
]

print(sorted(user, key=lambda n: n['username']))

musicas = [
    {'nome': 'Fome do cão', 'qtd': 344},
    {'nome': 'Vamos invadir', 'qtd': 2},
    {'nome': 'Born this way', 'qtd': 123},
    {'nome': 'Mr. Brightside', 'qtd': 100}
]

print(sorted(musicas, key=lambda qtd: qtd['qtd']))
