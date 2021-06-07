'''
LEITURA DE ARQUIVOS

Para ler um conteudo de arquivo em Python,
utilizamos a função integrada open()

open() = na forma mais simples de utilização nos passamos
apenas um parametro de entrada (obrigatório), 
que neste caso é o nome do arquivo a ser lido. 
Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

Obs. Por padrão, a função open() abre o arquivo para leitura.
Este arquivo deve existir, ou então, teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r = Modo de Leitura. r = read()

'''

arquivo = open(
    'c:\\Users\\pedro\\Python Projects\\estudo_python_geek\\venv\\Scripts\\13_secao\\texto.txt')

# print(arquivo)

# print(type(arquivo))

# Para ler o conteudo de um arquivo, após sua abertura, devemos utilizar a função read()

print(arquivo.read())

print(arquivo.read())  # Não retorna nada. Ja fez a leitura no primeiro read()


# obs. o Python utiliza o recurso cursor para trabalhar com arquivos.
# Esse cursos funciona como o cursos quando estamos escrevendo

# obs. A função read() le todo o conteudo do arquivo
