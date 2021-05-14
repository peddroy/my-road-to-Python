'''

FUNÇÕES COM RETORNO

numeros = [1, 2, 3]

ret_pop = numeros.pop()
print(f'O retorno de pop é: {ret_pop}')

ret_print = print(numeros)
print(f'O retorno de print é: {ret_print}')

#
# def quadrado_de_7():
    # print(7 * 7)
#
# quadrado_de_7()
#
# ret = quadrado_de_7()
# print(f'O retorno é {ret}')

#obs.  em Python, quando uma função não retorna nenhum valor, o retorno é None

#vamos refatorar a função para retornar um valor
#funções em Python que retornam valores devem retornar estes valores com a palavra reservada return
#não precisamos necesariamente criar uma variavel para receber o retorno de uma função
#Podemos passar a execução da função para outras funções

def quadrado_de_7():
    return 7 * 7



ret = quadrado_de_7()
print(f'O retorno é {ret}')
print(quadrado_de_7())
print(quadrado_de_7() + 1)

# Refatorando a primeira função

def diz_oi():
    return 'Oi! '

alguem = 'Pedro'

print(diz_oi() + alguem)

Obs.: Sobre a palavra reservada return
1. finaliza a função, sai da execução da função
2. Podemos ter em uma função diferentes returns
3. Podemos em um função retornar qualquer tipo de dados e ate mesmo multiplos valores

Exemplo 1 - finaliza a função, sai da execução da função

def say_hi():
    print('estou printando primeiro')
    return 'Oi!'
    print('estou printando primeiro')


print(say_hi())


Exemplo 2 - Podemos ter em uma função diferentes returns


def new_func():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(new_func())


Exemplo 3 - Podemos em um função retornar qualquer tipo de dados e ate mesmo multiplos valores


def another_func():
    return 2, 3, 4, 5


num1, num2, num3, num4 = another_func() # desempacotando

print(num1, num2, num3, num4)

print(another_func())


#Vamos criar uma função para jogar a moeda (cara ou coroa)

from random import random


def toss_coin():
    #Gera um número pseudo-aleatoria (existe repetição) entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(toss_coin())

# Refatorando o código


def toss_coin():

    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(toss_coin())


'''

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária


def is_odd():
    numero = 6
    if numero % 2 != 0:
        return True
    else:
        return False


print(is_odd())


# Refatorando

def is_odd():
    numero = 6
    if numero % 2 != 0:
        return True
    return False


print(is_odd())