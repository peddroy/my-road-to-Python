'''
REDUCE

A partir do Python 3 o reduce() não é uma função integrada (builtin)

É necessário importar esta função a partir do módulo 'functools'

Guido Von Rossum: 'Utilize a função reduce() se você realmente precisar.
Em todo caso, 99% das vezes um loop for é mais legível.

PARA ENTENDE REDUCE()

Imagine que você tem uma coleção de dados

dados = [a1, a2, a3, ... an]

E você tem uma função que recebe dois parametros:
def função(x, y):
    retur x * y

Assim como map() e filter(), o reduce() recebe dois parametros: função e iteravel

reduce(função, dados)

A função reduce() funciona da seguinte forma:
Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
Passo 2: res2 = f(res1 , a3)  # Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda o resultado
.
.
.
Passo N: resn = f(resm, an)

Ou seja, em cada passo ela aplica função passando como primeiro argumento o resultado  da aplicação anterior.
No final o reduce() irá aplicar o resultado final.

'''

# Vamos utilizar reduce() para multiplicar todos os itens de uma lista

from functools import reduce

dados = [1, 2, 3, 4, 5, 6]

multi = lambda x, y: x * y

multiplying = reduce(multi, dados)

print(multiplying)

# Utilizando loop padrão

total = 1

for i in dados:
    total = total * i

print(total)