"""

LIST COMPREHENSION - PARTE 1

Utilizando List Comprehension podemos podemos gerar novas listas com dados processados a partir de outro iteravel.

Sintaxe de List Comprehension

[dado for dado in interavel]

numeros = [1, 2, 3, 4]

res = [numero * 10 for numero in numeros]

print(res)


def quadrado(valor):
    return valor * valor


res = [quadrado(numero) for numero in numeros]  # utilizando função

print(res)

Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:
1. Primeira parte: for numero in numeros
2. Segunda parte: numero * 10


# List Comprehensions versus Loop

# Exemplo com Loop
numero_dobrado = []

for numero in [1, 2, 3, 4]:
    numero_dobrado.append(numero * 2)

print(numero_dobrado)

# List Comprehension
print([numero * 2 for numero in [1, 2, 3, 4]])

nome = 'Pedro Araujo'

print([letra.upper() for letra in nome])


def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigas = ['jessica', 'samara', 'suellen', 'jennifer']

print([caixa_alta(nome) for nome in amigas])

print([numero * 3 for numero in range(1, 10)])

print([bool(valor) for valor in [0, [], '', True, 1, 2, 3]])

print([str(num) for num in [1, 2, 3, 4]])




////////// LIST COMPREHENSION - PARTE 2 //////////



Podemos adicionar estruturas condicionais às lists comprehensions

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# refatorar

# Qualquer numero par modulo de 2 é 0 e 0 em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer numero impar modulo de 2 é 1 e 1 em Python é True.
impares = [numero for numero in numeros if numero % 2]


# estudo a parte if e if not
par = 2
impar = 3

if impar % 2:
    print(par)

# Outro exemplo:
numeros = [1, 2, 3, 4, 5, 6]

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)



/// YOUTUBE



l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ex1 = [(v * 2, v2) for v in l1 for v2 in range(3)]

l2 = ['Luiz', 'Marta', 'Maumau']

ex2 = [letra.replace('a', '@') for letra in l2]
ex3 = [letra.replace('a', '@').upper() for letra in l2]
print(ex3)


tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

exe4 = [(y, x) for x, y in tupla]
exe5 = dict(exe4)

print(exe5)

l3 = list(range(100))
exe6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(exe6)

exe7 = [v if v % 3 == 0 else 'Não é' for v in l3]
exe8 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(exe7)



linhas_colunas = [
    (x, y)
    if y != 2 else (x, y * 100)
    for x in range(1, 6)
    for y in range(1,4)
    if x != 2
]

print(linhas_colunas)

# String
string = 'Pedro Araujo'
numero_letras = 5
nova_string = '.'.join([
    string[indice:indice + numero_letras]
    for indice in range(0, len(string), numero_letras)
])

print(nova_string)
"""


nomes = ['luiz', 'maria', 'jose', 'carmelita', 'suavita']
novos_nomes = [f'{nome[:-1].lower()}'f'{nome[-1].upper()}' for nome in nomes]

print(novos_nomes)

numeros = [[numero, numero **2] for numero in range(10)]
print(numeros)


numeros = [[numero, numero **2] for numero in range(10)]
flat = [y for x in numeros for y in x]
print(flat)
