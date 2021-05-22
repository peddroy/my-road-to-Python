'''

TRY/EXCEPT

Utilização o bloco try/except para tratar erros que podem ocorrer no nosso codigo
Previnindo assim que o programa pare de funcionar e 
o usuário receba mensagem de erros inesperadas

A forma geral mais simples é: 

try:
    // execução problemática
except:
    // o que deve ser feito em caso de problemas


Exemplo 1: Tratando um erro generico

try:
    colore()
except:
    print('Deu problema aqui')


Exemplo 2: Tratando um erro generico

try:
    le(5)
except:
    print('Deu problema aqui')


Tratar erro de forma generica não é a melhor forma, é melhor tratar de forma especifica

# Exemplo 3: Tratando um erro especifico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')


try:
    len(5)
except NameError:
    print('Você está utilizando uma função inexistente')


# Exemplo 4: Tratando um erro especifico

try:
    len(4)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Exemplo 5: Efetuando diversos tratamentos

try:
    print('geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f"Deu TypeError: {errb}")
except:
    print('Deu erro diferente')

'''

# Exemplo 6


def pega_valor(dic, chave):
    try:
        return dic[chave]
    except KeyError:
        return None


dic = {'nome': 'geek'}

print(pega_valor(dic, 'game'))
