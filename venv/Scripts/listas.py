#LISTAS




lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
lista7 = [1, 2.38, 'Geek', True, 'D', [1, 2, 3]]
cores = ['verde', 'amarelo', 'azul', 'branco']
lista8 = [1, 7, 5, 6, 12, 16, 5, 9, 8, 5]

'''

Listas em Python funcionam como vetores e matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e tambem de podermos colocar QUALQUER tipo de dado

Em C/Java os arrays
Possuem tamanho e tipo de dado fixo
Ou seja, se você criar um array do tipo int e com tamanho cinco, este array sempre será do tipo inteiro
e poderá ter sempre no máximo cinco valores.

Em Python
DINÂMICO:
não possue tamanho fixo 




lista2 = list(range(11))
# print(listax)
listay = list('Pedro Araujo')
# print(listay)
#
# if 8 in listax:
#     print('encontrei')
# else:
#     print('nada')
#
# nome = list[x]

print(lista2)
lista2.append(42)
print(lista2)
lista2.append([12, 14,16]) # coloca a lista como elemento unico (sublista), vai sempre pro final
print(lista2)
lista2.extend([1, 2, 16]) # coloca cada elemento da lista como valor adicional a lista
print(lista2)

lista2.extend('geek')
print(lista2)

lista2.insert(2, 'geek')
print(lista2)

listaalfa = listay + lista2
print(listaalfa)

lista2.extend(listay)
print(lista2)

listamano = list('Manowar')
# listamano.reverse()
listamano.sort(reverse=True)
print(listamano)
print(len(listamano))


#POP

listamano.pop()
print(listamano)

listamano.pop(2)
print(listamano)


#SPLIT
# por padrão o split separa por espaços cada elemento

filme = 'O dia mais legal de todos'
print(filme)
filme = filme.split()
print(filme)
print(filme[3])

filme = 'O,dia,mais,legal,de,todos'
print(filme)
filme = filme.split(',') #setar o separador como ','
print(filme)
print(filme[3])




#CONVERTENDO LISTA EM STRING
#abaixo estamos falando: pega a lista6, coloca espaço entre cada elemento e converte para string
print(lista6)
curso = ' '.join(lista6)
print(curso)

curso = '-'.join(lista6)
print(curso)

#IMPRIMIR TIPO DE DADO
#lista aceita qualquer tipo de dado
print(type(lista7))


#ITERAR SOBRE LISTAS
#utilizando FOR
for elemento in lista7:
    print(elemento)

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)



#utilizando WHILE

carrinho = []
produto = ''

while produto != 'sair':
    print("Digite o nome do produto ou então 'sair': ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


#UTILIZANDO VARIAVEIS A LISTAS
#passando valores fixos dentro da lista
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

#passando variáveis dentro da lista
numeros = [num1, num2, num3, num4, num5]
print(numeros)

#Fazemos acesso aos elementos de forma indexada

#para entender o acesso aos elementos pensar numa roda. ascendente positivo, descendente negativo
print(cores[-1])


cores = []
cor = ''

while cor != 'sair':
    cor = input("Digite a cor ou então 'sair': ")
    if cor != 'sair':
        cores.append(cor)

for cor in cores:
    if len(cor) > 2:
        print(cor)

print(cores[2])

indice = 0
while indice < len(cor):
    print(cores[indice])
    indice = indice + 1



#GERAR INDICE EM LOOP FOR

for indice, cor in enumerate(cores):
    print(indice, cor)

DiasSemana = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']

DiasSemana = list(enumerate(DiasSemana))
print(DiasSemana)



#LISTAS ACEITAM VALORES REPETIDOS

ListaRepetida = []

ListaRepetida.append(1)
ListaRepetida.append(1)
ListaRepetida.append(2)
ListaRepetida.append(2)

print(ListaRepetida)



#####METODOS NÃO TÃO IMPORTANTES
# Encontrar o indice de um elemento na lista
# Qual o indice do numero 6


print(lista8.index(6))

#obs.: se não tiver o valor na lista será apresentado erro.
#obs.2: se existir valor repetido retorna o primeiro

#Podemos fazer a busca dentro de um range (somente seta início)
print(lista8.index(5, 4)) #o valor 5 é buscado a partir do indice 4

#Podemos fazer a busca dentro de um range (seta início e fim)
print(lista8.index(5, 4, 7)) #o valor 5 é buscado a partir do indice 4

#REVISÃO DE SLICING

# list[inicio:fim:passo]
# range(inicio:fim:passo)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Slice com parametro de inicio
print(lista[2:])
print(lista[-2:])

#Slice com parametro de fim
print(lista[:2])
print(lista[:-2])

#Slice com parametro de passo
print(lista[2:8:2])
print(lista[::-2])

nome = 'Programação em Python: Essencial'
print(nome[::-1])

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes.reverse()
print(nomes)

print(sum(lista1))
print(max(lista1))
print(min(lista1))
print(len(lista1))


#Converter listas em tupla

print(lista1)
tupla = tuple(lista1)
print(tupla)
print(type(tupla))


#Desempacotamento de lista
#obs.: tem que ter a mesma quantidade de elementos e variáveis

listax = [1, 2, 3]
print(listax)
num1, num2, num3 = listax
print(num1)
print(num3)
print(num2)

#Copiando uma lista para outra (Shallow Copy and Deep Copy)
#com o copy() as listas ficam independentes, modifica uma, a outra se mantem. Isso é chamado de Deep Copy em Python
#com a atribuição de uma lista em outra, quando modifica uma a outra tbm se modifica. Isso é chamado de Shallow Copy em Python
#Forma 1 - Deep Copy

print(listax)

ListaCopiada = listax.copy()
print(ListaCopiada)

ListaCopiada.append(4)
print(ListaCopiada)


#Forma 2 - Shallow Copy

listax = [1, 2, 3]
print(listax)

nova = listax
print(nova)

nova.append(7)

print(listax)
print(nova)



'''

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
# lista3 = []
# lista4 = list(range(11))
# lista5 = list('Geek University')
# lista6 = ['Programação', 'em', 'Python:', 'Essencial']
# lista7 = [1, 2.38, 'Geek', True, 'D', [1, 2, 3]]
# cores = ['verde', 'amarelo', 'azul', 'branco']
# lista8 = [1, 7, 5, 6, 12, 16, 5, 9, 8, 5]


#ITERAR SOBRE LISTAS
#utilizando FOR
# for elemento in lista7:
#     print(elemento)

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

soma = ''
# for elemento in lista2:
#     print(elemento)
#     soma = soma + elemento
# print(soma)


