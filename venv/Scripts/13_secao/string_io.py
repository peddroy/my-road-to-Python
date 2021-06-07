'''
STRING IO

Atenção: Para ler ou escrever dados em arquivos do sistema operacional
o software precisa ter permissão:
    - Permissão de Leitura do arquivo
    - Permissão de Escrita do arquivo

StringIO - utilizado para ler e criar arquivos em memoria



'''

# primeiro fazemos o import
from io import StringIO

mensagem = 'esta é apenas uma string normal\n'

# podemos criar um arquivo em memoria ja com a string inserida
# ou mesmo vazio para inserirmos texto depois

arquivo = StringIO(mensagem)
# é equivalente ao arquivo = open('arquivo.txt', 'w')

# agora tendo o arquivo podemos utilizar o que ja sabemos sobre leitura/escrita

print(arquivo.read())

arquivo.write('testiculo legal, hein?')


# podemos movimentar o cursor
arquivo.seek(2)

print(arquivo.read())
