'''
REVERSED()

Não confundir reversed() com reverse().
A função reverse() é específica para listas.
Já a função reversed() funciona para qualquer iteravel.
A função reversed() retorna um iteravel do tipo List Reverse Iterator


'''

lista = [1, 2, 3, 4, 5, 6, 7, 8]

res = reversed(lista)

print(res)
print(type(res))

print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))  # set não tem ordem definida


# Podemos iterar sobre um reversed()

nome = 'Altemar Dutra'

for letra in reversed(nome):
    print(letra, end='',)

# outro modo
print()
# (o join pega uma lista de string e junta tudo numa string)
print(''.join(list(reversed(nome))))

# Em string podemos
print(nome[::-1])

# podemos utilizar o reversed para fazer um loop for reverso
for i in reversed(range(1, 11)):
    print(i)
