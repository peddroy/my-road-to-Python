'''
MODOS DE ABERTURA DE ARQUIVO

r - abre para leitura
w - abre para escrita (sobrescreve caso o arquivo ja exista)
x - abre para escrita (falha se na existit)
a - abre pra escrita se ja existir arquivo add no final (a ded append)
+ - abre para o modo atualização: abertura e escrita

# with open('newtxt.txt', 'x') as arquivo:
#     arquivo.write('massoterapia')

with open('novissimotexto.txt', 'x') as arquivo:
    arquivo.write('newba')

'''

with open('novissimotexto.txt', 'a+') as arquivo:
    arquivo.write('isso aqui é boasdfasdfasdfasdf m de mais')
