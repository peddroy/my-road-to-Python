'''
MODULOS BUILT-IN

São módulos integrados que já vem instalados no Python

# Utilizando alias (apelidos) para módulos e funções

import random as rdm

print(rdm.random())


# Podemos importar todas as funções de um módulo utilizando asterisco

from random import *  # Deste modo não precisa utilizar o random.random()

print(random())



from random import randint as rdi, random as rdm

print(rdi(2, 7))
print(rdm())

'''


# Quando há muitas funções importadas de um mesmo módulo usamos tuple

from random import (
    random,
    randint,
    choice,
    shuffle,
    uniform
)

print(random())
