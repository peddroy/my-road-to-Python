'''

BLOCO WITH

1 - Abrimos o arquivo
2 - Manipulamos o arquivo
3 - Fechamos o arquivo 

O bloco with é utilizado para criar um contexto de trabalho
onde os recursos utilizados são fechados apos o bloco with

'''
# É a forma Pythonica de se trabalhar com o arquivo
# Com o with não precisa fechar  - ele só é aberto dentro do contexto

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
