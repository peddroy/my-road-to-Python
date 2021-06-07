'''
INSTALANDO E UTILIZANDO MODULOS EXTERNOS

Utilizamos o gerenciador de pocotes Python PIP - Python Installer Package

Podemos conhecer todos os pacotes externos e oficiais Python em:
https://pypi.org/

Instalar COLORAMA
Permitir impressão de textos coloridos no terminal

No terminal pip install colorama

UTILIZANDO O PACOTE COLORAMA

from colorama import init, Fore, Back

init()

print(Fore.CYAN + 'Texto aqui')
print(Back.YELLOW + 'Texto aqui')

'''

import pydf

pdf = pydf.generate_pdf(
    '< h1 > this is html < /h1 >')

with open('meuarquivo.pdf', 'wb') as f:
    f.write(pdf)
