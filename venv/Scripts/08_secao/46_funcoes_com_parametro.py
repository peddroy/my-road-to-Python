'''

FUNÇÕES COM PARAMETRO DE ENTRADA

def quadrado(numero):
    return numero * numero

print(quadrado(2))
print(quadrado(3))
print(quadrado(8))


def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print(f'Viva o {aniversariante}')


cantar_parabens('Marcos')

# Funções com n entradas

def soma(a, b):
    return a + b

def multiplica (a, b):
    return a * b

def outra(a, b, msg):
    return (a + b) * msg

a = 2
b = 3

print(soma(a, b))
print(multiplica(a, b))
print(outra(a, b, 'robert '))



#diferençla entre parametros e argumentos
# parametros = são variaveis declaradas na definição de uma função
# argumentos = são dados passados durante a execução de uma função

# erros quando a quantidade de argumentos é diferente da quantidade de parametros

#a ordem dos parametros importa

# Argumentos nomeados (Keyword Arguments)

'''


def nome_completo(nome, sobrenome):
    print(f'O nome completo é {nome} {sobrenome}')


nome = 'Carla'
sobrenome = 'Carlson'

nome_completo(nome, sobrenome)
nome_completo(nome=nome, sobrenome=sobrenome)
nome_completo(nome='June', sobrenome='Ribeiro')
nome_completo(sobrenome='Jemima', nome='Santo Antonio')


def soma_impares(numeros):
    total = 0
    for i in numeros:
        if i % 2 != 0:
            total = total + i
    return total


lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))
