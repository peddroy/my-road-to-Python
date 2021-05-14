'''
ENTENDENDO **KWARGS

Poderiamos chamar de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parametro, mas diferente do *args que coloca os valores extras como tupla,
o **kwargs exige que coloquemos parâmetros nomeados e transforma esses parametros extras em dicionário


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'o cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(josue='verde', marilicia='amarelo', claudio='serpente')



def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento especial Phytonico'
    elif 'geek' in kwargs:
        return f"olá {kwargs['geek']}, legal!"
    else:
        return 'sei não'

print(cumprimento_especial())
print(cumprimento_especial(geek='seba'))
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(seboreica='marshmallow'))

# Nas nossas funções podemos ter nesta ordem:

- parametro obrigatório
- *args
- parametro default
- **kwargs


def minha_funcao(nome, idade, *args, solteiro=False, **kwargs):
    print(f'Nome {nome} e idade {idade}')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao('Julia', 9,)
minha_funcao('Julia', 9, 4, 5 ,6, solteiro=True)
minha_funcao('Julia', 9, 'samba', jeny='Silva', marta='campo belo')
minha_funcao('Julia', 9, 2, 4, 5, mes='janeiro', ano='2020')


# Porque é importante manter a ordem dos parametros na hora da declaração

# correto
def mostra_info(a, b, *args, instrutor='geek', **kwargs):
    return a, b, args, instrutor, kwargs


print(mostra_info(1, 2, 3, sobrenome='University', cargo='instrutor'))

# INcorreto - invertendo os parametros
def mostra_info(a, b, instrutor='geek', *args, **kwargs):
    return a, b, args, instrutor, kwargs

# aqui ele deixa o args vazio e passa para o default 'instrutor' o argumento 3
print(mostra_info(1, 2, 3, sobrenome='University', cargo='instrutor'))


'''

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome':'Felicity', 'sobrenome':'Jones'}
# colocar ** para desempacotar
print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 6]
tupla = (1, 2, 3)
conjunto = {4, 5, 6}
soma_multiplos_numeros(*lista) # só desempacotou nos obrigatórios, não usamos *args
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

# para dicionários utilizar duplo*

# Os nomes das chaves tem que ser os mesmos dos parametros da função
dicionario = {'a':1,'b':3, 'c':5}

soma_multiplos_numeros(**dicionario)

