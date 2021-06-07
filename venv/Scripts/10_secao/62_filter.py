'''
FILTER

filter() serve para filtrar dados de uma determinada coleção
retorna um Filter Object



# biblioteca para trabalhar com dados estatísticos

import statistics

# dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# calculando a média usando a função mean()

media = statistics.mean(dados)
print(media)

# assim como map() o filter() também recebe dois parametros
# sendo, uma função e um iteravel

res = filter(lambda valor: valor > statistics.mean(dados), dados)
print(f'Primeiro: {list(res)}')
print(f'Segundo: {list(res)}') # lembrando que filter assim como map limpa a memoria depois de executado



# Utização para remoção de dados faltantes (limpeza de dados)

paises = ['', 'Brasil', '', 'Equador', '', 'Argentina', 'Chile', 'Uruguai', '', '', 'Venezuela']
print(paises)

res_um = filter(None, paises)
res_dois = filter(lambda pais: pais != '', paises)
print(list(res_um))
print(list(res_dois))

# A diferença entre map() e filter()

# map retorna valores
# filter sempre retorna True ou False, o booleano 
# faz o dado ser selecionado


# Exemplo mais complexo

usuarios = [
    {'username': 'samuel', 'tweets':['amo chocolate','bora lá']},
    {'username': 'carlinhah2o', 'tweets': ['hoje ta legal', 'sei não']},
    {'username': 'xhiui', 'tweets': []},
    {'username': 'santosoficial', 'tweets': []},
    {'username': 'nasmateparamimepara', 'tweets': ['gratiluz']}
]

res_map = map(lambda usuario: {'tweets': usuario['tweets']}, usuarios)
print(list(res_map))

res_fil = list(filter(lambda usuario: usuario['tweets'] != [], usuarios))
print(list(res_fil))

res_fil_dois = list(filter(lambda usuario: not usuario['tweets'], usuarios)) # veja exemplo com not
print('dois')
print(res_fil_dois)

traz_ativos = map(lambda pessoa: pessoa['username'], res_fil)
print(list(traz_ativos))

nomes = ['Vanessa', 'Ana', 'Ci']

# Utilizando filter e map

# Devemos criar uma lista contendo 'Sua instrutora é ' + nome,desde que nome maior que 5 caracteres.

nome_maior_cinco = map(lambda nomes: f'Sua instrutora é {nomes}', filter(lambda nome: len(nome) < 5, nomes))

print(list(nome_maior_cinco))

produtos = [
    {'nome_produto': 'cebola', 'preço_produto': 3.50},
    {'nome_produto': 'alho', 'preço_produto': 9.50},
    {'nome_produto': 'agrião', 'preço_produto': 4.50},
    {'nome_produto': 'arroz', 'preço_produto': 25.50},
    {'nome_produto': 'vinho', 'preço_produto': 123.50}
]

produto_menor_dez = map(
    lambda produto: 
    f"O produto com valor menor que R$10,00 é {produto['nome_produto']}", 
    filter(lambda produto: produto['preço_produto'] < 10, produtos))

print(list(produto_menor_dez))




from pprint import pprint
print = pprint
pprint = print

produtos = [
    {'nome': 'P1', 'preço': 59.60, 'peso': 1.350, 'variacoes': ['a', 'b']},
    {'nome': 'P2', 'preço': 69.60, 'peso': 2.250, 'variacoes': ['c', 'd']},
    {'nome': 'P3', 'preço': 79.60, 'peso': 3.150, 'variacoes': ['e', 'a']},
    {'nome': 'P4', 'preço': 89.60, 'peso': 4.050, 'variacoes': ['g', 'h']},
    {'nome': 'P5', 'preço': 99.60, 'peso': 5.950, 'variacoes': ['a', 'j']},
    {'nome': 'P6', 'preço': 09.60, 'peso': 6.850, 'variacoes': ['k', 'l']}
]
# FILTER
maior_vinte = filter(lambda produto: produto['preço'] < 20, produtos)
print(list(maior_vinte))


# FILTER COM MAP
maior_vinte = map(lambda produto: produto['nome'], filter(
    lambda produto: produto['preço'] < 20, produtos))
print(list(maior_vinte))


# FAZENDO COM LIST COMPREHENSION
maior_vinte_comprehension = [
    produto['nome'] for produto in produtos if produto['preço'] < 20]
print(maior_vinte_comprehension)


print('# FAZENDO COM FOR PADRÃO')
maior_vinte_for = []
for produto in produtos:
    if produto['preço'] < 20:
        maior_vinte_for.append(produto['nome'])
print(maior_vinte_for)


# TENTATIVA DE FILTRAR A LISTA DENTRO DA BIBLIOTECA
# COM FOR PADRÃO
tem_variacao_a = []
for produto in produtos:
    for variacao in produto['variacoes']:
        if variacao == 'a':
            tem_variacao_a.append(produto['nome'])

print(tem_variacao_a)

# COM LIST COMPREHENSION

tem_variacao_a_comprehension = [
    produto['variacoes'] if produto['variacoes'] == 'a' else 'no' for produto in produtos]

print(tem_variacao_a_comprehension)

'''

print('ola')
