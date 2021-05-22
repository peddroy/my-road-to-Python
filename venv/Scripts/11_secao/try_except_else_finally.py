'''

TRY, EXCEPT, ELSE, FINALLY

Dica de quando e onde tratar o código
Toda ENTRADA deve ser tratada.

Obs. A função do usuário é destruir o sistema

try:
    num = int(input('Digite um numero: '))
except:
    print('Valor incorreto')
else:  # só é executado se não ocorrer o erro
    print(f'Você digitou o número {num}')

# Finally: O bloco é sempre executado com except ou não
# O finally geralmente é utilizado  pra fechar ou desalocar recursos
# Exemplo: Fechar conexão com banco de dados.

try:
    num = int(input('Digite um numero: '))
except:
    print('Valor incorreto')
else:  # só é executado se não ocorrer o erro
    print(f'Você digitou o número {num}')
finally:
    print('Sempre sou executado')


# Exemplo completo, mas errado


def dividir(a, b):
    return a / b


num1 = int(input('Digite o primeiro número: '))
try:
    num2 = int(input('Digite o segundo número: '))
except ValueError as err:
    print(f'Erro aqui ó: {err}')

try:
    print(dividir(num1, num2))
except NameError as err:
    print(f'Outro erro parça: {err}')


# Exemplo completo, pythonico


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return f'Não ta legal não'
    except ZeroDivisionError:
        return f'Não é possível dividir por 0'


num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

print(dividir(num1, num2))


# Exemplo completo genérico


def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return f'Não ta legal não'


num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

print(dividir(num1, num2))



'''

# Exemplo completo semigenérico


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Não ta legal não: {err}'


num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

print(dividir(num1, num2))
