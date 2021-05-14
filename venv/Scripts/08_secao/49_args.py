'''
ENTENDENDO O *ARGS

O *args é um parametro como qualquer outro.
Isso significa que você poderá chamar de qualquer coisa, desde que comece com asterisco.
Por convenção utilizamos o *args para definí-lo

Mas o que que é *args?
O parametro *args utilizado em uma função coloca os valores extras informados como entrada em uma tupla.
Lembre-se que tuplas são imutáveis.

def soma_todos(*args):
    return sum(args)


print(soma_todos(2, 4, 6, 7))


def verifica_info(*args):
    if 'Geek' and 'University' in args:
        return 'Legal'
    else:
        return 'Sei não'

print(verifica_info())
print(verifica_info(1, True, 3.6, 'Geek', 'University'))
print(verifica_info('marmelada', 'pastel de frango'))

'''




def soma_todos(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6]

print(soma_todos(numeros)) #erro
print(soma_todos(*numeros)) #colocando o * na frente da lista ele desempacota ela

#O asterisco serve para informar que estamos passando uma coleção de dados.
#Desta forma ele saberá que precisará desempacotar os dados antes