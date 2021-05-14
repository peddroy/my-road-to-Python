'''

MODO COLLECTIONS - DEFAULT DICT

https://docs.python.org/3/library/collections.html#collections.defaultdict

#Recap - Dicionários

dicionario = {
    'curso': 'Programação em Python: Essencial',
    'ano': 2021,
    'mes': 'Março'
}
print(dicionario)
print(dicionario['mes'])
print(dicionario['megadeth']) # Gera KeyErro - A chave não existe

Com Default Dict ao criar um dicionário nos informamos um valor default, podendo utilizar um lambda para isso
esse valor será utilizado sempre que não houver valor definido. Caso tentemos utilizar chave que não existe, essa chave será criada
e o valor default atribuido

OBS. Lambdas são funções sem nome quee podem ou não receber parametros de entrada
e retornar valores

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

print(dicionario['outro'])
#acessando o dicionario na chave 'outro' que não existe - em defaultdict retorna valor padrão
#quando se faz a busca por uma chave que não existe ele cria e coloca valor padrão

print(dicionario) # aqui exibe a chave outro que foi criada com valor default

'''

from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)

for k, v in s:
    d[k].append(v)

print(s)
print(d)

print(sorted(d.items()))

