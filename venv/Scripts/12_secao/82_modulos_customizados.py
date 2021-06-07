'''

MODULOS CUSTOMIZADOS

Como modulos são arquivos, 
todos os arquivos que criamos são módulos prontos para serem utilizados

IMPORTANDO UMA FUNÇÃO ESPECIFICA DE UM MODULO

from soma_impares import soma_impares

lista = [1, 2, 3, 4, 5, 6]

print(soma_impares(lista))


'''

# Importando todo o modulo temos acessos a todos os elementos do modulo


from arquivo_base_82 import cidades, c_para_f
import arquivo_base_82 as si

print(si.lista)

print(si.tupla)

print(list(map(c_para_f, cidades)))
