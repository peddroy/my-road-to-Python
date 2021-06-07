'''

SEEK E CURSOR

seek() - é utilizado para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt')

print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek()
# A função seek() é utilizada para movimentação do cursor pelo arquivo.
# Ela recebe um parametro que indica onde queremos colocar o cursor

arquivo.seek(15)

print(arquivo.read())

# readline() = Função que lê o arquivo linha a linha

ret = arquivo.readline()

print(type(ret))

print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())


# readlines() = coloca cada linha em uma lista

# print(arquivo.readlines())

print(len(arquivo.readlines()))

Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco do computador e nosso programa. Essa conexão é chamada de streaming.
Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão.
Para isso usamos a função close()

Passos para se trabalhar com um arquivo:
1 - Abrir o arquivo
2 - Trabalhar com o arquivo
3 - Fechar o arquivo


# 1 - Abrir o arquivo
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo
print(arquivo.readlines())
print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado (False)

# 3 - Fechar o arquivo
arquivo.close()
print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado (True)

# Se tentarmos manipular o arquivo após o seu fechamento, teremos um ValueError


'''
arquivo = open('texto.txt')

print(arquivo.read(50))  # exibe 50 caracteres
print(arquivo.read(50))  # exibe 50 caracteres
