'''
DICIONÁRIOS

Obs.: Em algumas linguagens o dícionário é conhecido como mapas

Dicionário são coleções do tipo chave/valor


Dicionários são representados por {}

- Chave e valor são separados por :
- Tanto chave e valor podem ser de qualquer tipo de dados
- Podemos misturar tipos de dados



#CRIAÇÃO DE DICIONÁRIOS
# FORMA 1 - MAIS COMUM

print(type({}))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

#FORMA 2 - MENOS COMUM

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

#ACESSANDO ELEMENTOS
#FORMA 1 - ACESSANDO VIA CHAVE, DA CHAVE/VALOR, DA MESMA FORMA QUE LISTA/TUPLA

print(paises['br'])
print(paises['py'])

#print(paises['ru'])#Caso acesso a uma chave que não existe exibirá o erro KeyError

#FORMA 2 - RECOMENDADA - ACESSANDO VIA GET

print(paises.get('br'))
print(paises.get('ru'))

#Tipo de dado NONE = Tipo sem tipo
numeros = None
print(numeros)
print(type(numeros))

#Quando utilizamos
#Quando criamos uma variável qe queremos inicializa-la com tipo sem tipo, antes de recebermos um valor final

#o tipo None é sempre considerado como falso

#Caso o get não encontre o objeto com a chave informada será retornado um valor None e não será gerado KeyError

pais = paises.get('ru')

if pais:
    print(f'Encontrei o pais {pais}')
else:
    print(f'Não encontrei o pais')


pais = paises.get('br', 'Não encontrei')
#Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

print(pais)


#Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)


if 'ru' in paises:
    russia = paises['ru']


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

#podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive (list, tuple , dict) como chave de dicionarios

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova Iorque',
    (37.7748, 122.4194): 'Escritório em São Paulo',
}

#tuplas são interessantes para serem utilikzadas como chaves de dicionarios pois elas são imutaveis, não se pode alterar, exlcuir e nem modificar

print(localidades)
print(type(localidades))
#Adicionar elementos a um dicionário

receita = {
    'jan': 100,
    'fev': 120,
    'mar': 300
}

print(receita)
print(type(receita))

#FORMA 1

receita['abr'] = 350

print(receita)

#FORMA 2

novo_dado = {'mai': 500}

receita.update(novo_dado)

print(receita)

receita.update({'jun': 550})

print(receita)

# Atualizando dados em um dicionário

#Forma 1

receita['mai'] = 700
print(receita)

# Forma 2

receita.update({'mai': 900})
print(receita)

# Conclusão 1: Utilizamos a mesma forma para adicionar ou atualizar dados em um dicionário
# Conclusão 2: Não temos chaves repetidas em um dicionario

# Remover dados em um dicionario

#Forma 1 - mais comum

print(receita)
receita.pop('jan')
print(receita)

print(receita)
ret = receita.pop('mar')
print(ret)
print(receita)

#Obs.1: Precisamos sempre informar a chave, caso não encontre um KeyError é retornado
#Obs.2: Ao removermos um objeto, o valor deste objeto é retornado

# Forma 2

del receita['mai']
print(receita)

# Ecommerce
# FORMA 1
#Utilizando listas

carrinho = []

produto1 = ['arroz', 1, 12.00]
produto2 = ['feijão', 2, 9.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#teriamos que saber o indice de cada elemento do produto

# FORMA 2
# Utilizando tuplas

carrinho = ()

produtoa = ('macarrão', 2, 4.50)
produtob = ('alho', 7, 10.00)

carrinho = produtoa, produtob

print(carrinho)

#teriamos que saber o indice de cada elemento do produto

# FORMA 3
# Utilizando dicionarios

carrinho = []

produto1 = {
    'nome': 'arroz',
    'quantidade': 1,
    'preço': 24.00
}

produto2 = {
    'nome': 'macarrão',
    'quantidade': 2,
    'preço': 4.00
}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#desta forma, adicionamos e removemos produtos no carrinho
# e em cada produto podemos ter certeza do que se trata a informação



# Metodos de dicionário

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))


# Limpar o dicionario

d.clear()

print(d)

# Copiando um dict para outro
# Forma 1 - Deep copy

novo = d.copy()

print(novo)

novo['d'] = 1

print(d)
print(novo)

#Forma 2 - Shallow copy

novo = d

print(novo)

novo['e'] = 5

print(d)
print(novo)


'''

# Metodos de dicionário

# Forma não usual de criação de dicionario

outro = {}.fromkeys('a', 'b')

print(outro)

pessoa = {}.fromkeys(['nome', 'email', 'telefone', 'endereço'], 'desconhecido')

print(pessoa)

# o metodo fromkeys recebe dois parametros: um iteravel (iterar em cada um dos elementos da lista, por exemplo) e um valor
# ele gera pra cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)
# dicionario não tem repetição de chave

novo = {}.fromkeys(range(1, 10), 'novo')
print(novo)


teste
