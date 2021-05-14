'''

FUNÇÕES COM PARAMETRO PADRÃO (Default Parameters)

- São funções onde a passagem de parametro é opcional

Exemplo de função com parametro opcional:
print('testes')
print()

Exemplo de função com parametro obrigatório


def quadrado(numero):
    return numero ** 2


print(quadrado(2))



#aqui foi configurado um padrão para o parametro potencia, se user não passar nenhum argumento ele utiliza o default


def potencia(numero, potencia=2):
    return numero ** potencia


print(potencia(2))

# Em Python os valores padrão devem sempre estar no final da declaração
#erro:


def teste(num=1, potencia): #Erro
    return num ** potencia


#exemplo mais complexo


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome == "Geek":
        return 'Bem vindo Geek'
    else:
        return f'Fala {nome}!, Que tu quê?'


print(f'primeiro {mostra_informacao()}')
print(f'segundo {mostra_informacao("Geek")}')
print(f'terceiro {mostra_informacao(nome="Geek", instrutor=True)}')
print(f'quarto {mostra_informacao("Cleide")}')
print(f'quinto {mostra_informacao(nome="Christina Aguiller")}')


Por que utilizar parametros padrão?
- maior flexibilidade nas funções
- evita erros com parametros incorretos
- nos permite trabalhar com exemplos mais  legiveis do código

Quais  tipos de dados  podemos utilizar como valores default para parametros?
- Qualquer tipo de dado: numero, string, float, bollean, listas, tuplas, dicionarios, funções.


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def sub(num1, num2):
    return num1 - num2


print(soma(1, 2))
print(mat(2, 4))
print(mat(2, 6, sub))


# Escopo - Variáveis global e locals()
# Se puder evite variaveis globais

instrutor = 'Geek'

def diz_oi():
    dia = 'bom dia!'
    return f'Oi {instrutor}, {dia}'

#caso variavel com mesmo nome, a local tem preferencia sobre a global

print(diz_oi())
# print(dia) #Erro: é uma variavel local da função diz_oi()


total = 0

def soma():
    total = total + 12 (a variavel precisa ser inicializada dentro da função)
    return total


print(soma())

total = 0

def incrementa():
    global total #agora a variavel está acessando o valor global
    total = total + 12
    return total


print(incrementa())
print(incrementa())
print(incrementa())


# Podemos ter funções que são declaradas dentro de funções e tambem tem uma forma especial de escopo de variavel


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())

'''




def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def sub(num1, num2):
    return num1 - num2


print(soma(1, 2))
print(mat(2, 4))
print(mat(2, 6, sub))