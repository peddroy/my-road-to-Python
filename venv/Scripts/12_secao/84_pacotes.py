'''

PACOTES

Modulo é apenas um arquivo Python que pode ter diversas funções para utilizar:
Pacotes - é um diretório contendo uma coleção de modulos

Nas versão 2.x so Python, um pacote deveria conteter dentro dele
um arquivo chamado __init__.py
Nas versões do Python 3.x, não é mais obrigatória a utilização 
deste arquivo, mas normalmente ainda é utilizado para manter compatibilidade


'''

from geek.university import geek3, geek4
from geek import geek1, geek2

print(geek1.pi)

print(geek1.funcao1(1, 5))

print(geek2.funcao2())


print(geek3.funcao3())

print(geek4.funcao4())
