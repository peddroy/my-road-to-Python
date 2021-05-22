'''
MODULO RANDOM

Em Python módulos não mais são do que outros arquivos Python

O módulo Random possui diversas funções pra geração de números pseudo-aleátorios

existem duas formas de se utilizar um módulo ou função

# Formma 1: Importar todo o módulo (Não recomendado)



# ao realizar o import de todo o módulo todas as
# funções, atributos, classes e propriedades que
# tiverem dentro do módulo ficarão disponíveis,
# ficaram em memória
# Caso você saiba quais funções voce precisa utilizar
# deste modulo então esta não seria a forma ideal de utilização

print(dir(random))
print(help(random.random()))


'''
import random

# O random() Gera um numero pseudo aleátorio entre 0 e 1

print(random.random())

# Veja que ao utilizar a função random() do pacote random
#  nós colocamos o nome do pacote e o nome da função separados por ponto.

# Não confundir a função random() com o pacote random. Temos o parenteses após a função
# A função random() é somente uma função dentro do pacote random
