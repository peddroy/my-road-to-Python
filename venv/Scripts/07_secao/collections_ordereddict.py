'''

MODO - COLLECTIONS - ORDERED DICT

https://docs.python.org/3/library/collections.html#collections.OrderedDict

#Em um dicionario, a ordem de inserção dos elementos não é garantida

d = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

print(d)

for chave, valor in d.items():
    print(f'chave = {chave} e valor = {valor}')

#com ordered dict é garantido a ordem de inserção de elementos

d = OrderedDict({
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
})

for chave, valor in d.items():
    print(f'{chave} e {valor}')

from collections import OrderedDict

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) #True or False??

# O Dict comum não se preocupa com ordenção, por isso os dois dicionário acima são iguais

# Com Ordered Dict

od1 = OrderedDict({'a': 1, 'b': 2})
od2 = OrderedDict({'b': 2, 'a': 1})

print(od1 == od2)


'''

