'''

Debundo com Python Debbuger


# A utilização de print() para debugar cógido é uma prática ruim


def dividir(a, b):
    print(f'a = {a} e b = {b}')
    try:
        return a / b
    except (ValueError, ZeroDivisionError) as err:
        return f'Eita! Ocorreu um erro {err}'


print(dividir(7, 0))


# No Pycharm utilizar breakpoint

# Outra maneira é importar o pdb e utilizar o set_trace()
# # Comandos básicos do PDB
# l = lista onde estamos no código
# n = próxima linha
# p = imprime variavel
# c = continua execução - finaliza debug

import pdb


def dividir(a, b):
    pdb.set_trace() # da pra fazer o import na mesma linha import pdb; pdb.set_trace()
    try:
        return a / b
    except (ValueError, ZeroDivisionError) as err:
        return f'Eita! Ocorreu um erro {err}'


print(dividir(7, 0))

# Porque fazer o import e o set_trace() na mesma linha
# os importantes são feitos sempre no começo do arquivo
# como o debug é utilizado momentaneamente vc insere e depois retira



'''


# A partir do Python 3.7 o pdf foi incorporado como função builtin
# basta chamar por breakpoint()


def dividir(a, b):
    breakpoint()
    try:
        return a / b
    except (ValueError, ZeroDivisionError) as err:
        return f'Eita! Ocorreu um erro {err}'


print(dividir(7, 0))
