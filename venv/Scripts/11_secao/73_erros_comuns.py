'''

ERROS MAIS COMUNS EM PYTHON

É importe entender as saidas de erros geradas pelo código

Erros comuns
# 1 - SintaxError: Quando o python encontra erra de sintaxe.


def atibaia
return atibaia

def = 1

return

# 2 - NameError: ocorre quando uma variavel ou função não foi definida

print(geek)

geek()

a = 10

if a < 9:
    msg = 'Não entrei aqui'

print(msg)


3 - TypeError: Ocorre quando uma função/ação/operação
 é aplicado a um tipo errado

print(len(5))

print('geek' + [])

4 - IndexError: Ocorre quando tentamos acessar um elemento em uma lista
ou outro tipo de dado indexado utilizando um indice invalido

lista = ['Geek']

print(lista[2])


print(lista[0][5])

ValueError: Ocorre quando uma função/operação builtin recebe um argumento 
com tipo correto mas valor incorreto


print(int('geek'))

6 - KeyError: ocorre quando tentamos acessar um dicionário
 com uma chave que não existe

dic = {}

print(dic['y'])


7 - AttributeError - ocorre quando uma variavel não tem atributo/função

tupla = (11, 2, 5, 7, 14, 3)

print(tupla.sort()) # Não existe essa função pra tupla só lista

8 - IndentationError: ocorre quando não respeitamos a indentação do código

def mamamia():


print mamamia


Exceptions and Erros são sinonimos em programação

'''


def mamamia():


print(mamamia())
