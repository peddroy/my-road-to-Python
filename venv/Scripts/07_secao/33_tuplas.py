'''
### TUPLAS (TUPLE)

Tuplas são bastante parecidas com listas

Existe basicamente duas diferenças

1. As tuplas são representadas por ()
2. As tuplas são imutáveis. Isso significa que ao criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla

Cuidada 1 - As tuplas são representadas por (), mas se não tiver tbm gera uma tupla


tupla1 = (1, 2, 3)
tupla2 = 1, 2, 3

print(tupla1)
print(type(tupla1))

print(tupla2)
print(type(tupla2))

#Cuidado 2: Tuplas com um elemento

tupla3 = (3) #isso não é uma tupla
print(tu
dir(tuple)


#desempacotar tupla

tupla = ('Geek University', 'Programação em Python:', 'Essencial')

escola, curso, modulo = tupla

print(curso)
print(escola)
print(modulo)

você foi hckeado

tupla = 1, 2, 3, 4, 5, 6

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))


#Concatenação de tuplas

tupla1 = 1, 2, 3
print(tupla1)

tupla2 = 6, 7, 8
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

print(f'tupla 1: {tupla1}')
tupla1 = tupla1 + tupla3 #tuplas são imutaveis mas podemos sobreescrever seus valores
print(f'tupla 1 alterada: {tupla1}')

#Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3, 33, 66)

x = int(input('Digite um numero: '))
print(x in tupla)


#iterando sobre uma tupla

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y')

print(tupla.count('i'))

escola = tuple('Pedro Araujo') #converter string para tupla
print(escola)
print(escola.count('o'))


#Dicas na utilização de tupla

#Devemos utilizar tuplas sempre que não precisarmos modificar os dados contigos em uma coleção

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
meses.append('MartaRocha')

print(meses)

for indice, valor in enumerate(meses):
    print(indice, valor)

#O acesso a elementros de uma tupla também é semelhando a de uma lista

print(meses[5])

#iterar com while

i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

#Verificar em qual indice um elemento está na tupla

meses = ('Janeiro', 'Fevereiro', 'Julho', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses.index('Julho')) #caso não exista retorna um erro, caso exista mais de um retorna o primeiro
print(meses. index('Julho', 5)) # a partir do elemento 5

#Slicing
#tupla[inicio:fim:passo]

print(meses[2:4])
print(meses[::-1])

'''

#Por que utilizar tuplas
#1. Tuplas são mais rápidas do que listas. Maior performance.
#2. Tuplas deixam o código mais seguro. Por conta imutábilidade

#Copiando uma tupla para outra

tupla = 1, 2, 3
print(tupla)

nova = tupla #na tupla não temos o shallow copy. quando modifica uma a outra não modifica
print(nova)

outra = 6, 7, 8

nova = nova + outra

print(nova)
print(tupla) #não houve alteração da antiga








