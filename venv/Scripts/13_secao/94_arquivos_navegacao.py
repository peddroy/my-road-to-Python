'''

SISTEMA DE ARQUIVOS E NAVEGAÇÃO

Para fazer uso de manipulção de arquivos do sistema operacional, 
precisamos importar e fazer uso do modulo os

os - operating system

# pegar o path
# retorna o caminho absoluto
print(os.getcwd())  # Current Work Directory

# Para mudar de diretorio podemos usar o chdir()

os.chdir('..')

print(os.getcwd())


'''
# fazer import do móduolo

import sys
import os

# Retorna True
print(os.path.isabs("Users\\pedro\\"))

# Podemos idenficar o sistema operacionar com modulo os

print(os.name)  # Posix (Linus and Mac) nt (Windows)

# Podemos ter mais detalhes com uname()

# print(os.uname)


print(sys.platform)
