'''

UTILIZANDO LAMBDAS

expressões lambdas são funcções sem nome ou seja funções anonimas

comumente utilizada para fazer ordenação e filtragem

'''

def funcao(x):
    return 3 * x + 1

print(funcao(3))
print(funcao(7))

calc = lambda x: 3 * x + 2

print(calc(3))
print(calc(7))

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('  angelina', 'JOLIE'))
print(nome_completo(' FELICITY    ', 'jones    '))

amar = lambda: 'Como não amar Python'
calcum = lambda x: f'Esse é o {x}'
calcdois = lambda x, y: x + y
calctres = lambda x, y, z: (x + y) / z

print(amar())
print(calcum(10))
print(calcdois(10, 11))
print(calctres(5,5,2))

autores = ['Machado de Assis', 'Jose de Alencar', 'Rui Barbosa', 'Cecilia Meireles', 'Vinicius de Morais',
           'Clarice Lipector', 'Graciliano Ramos', 'Mario de Andrade']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

# Função Quadratica
# f(x) = a * x ** 2 + b * x + c

def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(1, 1, 1)(5))


