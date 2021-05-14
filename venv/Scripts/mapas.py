
'''

Mapas - Conhecidos em Python como Dicionários

Dicionários são representados por chaves


print(receita)

# Como iterar sobre dicinários

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R${receita[chave]},00')

#Acessando as chaves

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

#Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários

print(receita.items()) #É um dicinário que contem um lista com tuplas de chave/valor

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')



'''

receita = {
    'jan': 100.00,
    'fev': 200.00,
    'mar': 300.00,
    'abr': 400.00
}

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho

# #*para valores inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))