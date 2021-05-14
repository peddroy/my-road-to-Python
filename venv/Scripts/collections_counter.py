'''

MODULO COLLECTIONS - COUNTER

https://docs.python.org/3/library/collections.html
https://docs.python.org/3/library/collections.html#collections.Counter


Collections - conhecido como High-Performance Container Datatypes

O Counter recebe um iteravel como parametro e cria um objeto do tipo Collections Counter que é parecido com um dicionario
contendo como chave o elemento que passamos como parametro e como valor a quantidade de ocorrencias desse elemento


# EXEMPLO 1

#Realizando o import
from collections import Counter

#no exemplo é uma lista, mas poderia ser tupla, dicionario, string, conjunto - Qualquer iteravel
lista = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 5, 5, 1, 1, 1, 1, 5, 5, 5, 77, 77, 7, 76, 75, 45]

#Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

# # Counter({1: 8, 2: 5, 5: 5, 3: 2, 77: 2, 4: 1, 7: 1, 76: 1, 75: 1, 45: 1})
# Para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade de ocorrencia
# No exemplo o elemento 1 foi encontrado 8 vezes, o elemento 2 foi encontrado 5 vezes...


#Realizando o Counter no print

print(Counter('Pedro Araujo '))


'''

# EXEMPLO 2

#Realizando o import
from collections import Counter


# EXEMPLO 3

texto = """A Classe Ersatz Monarch foi uma classe de navios couraçados para a Marinha Austro-Húngara 
(imagem, estandarte naval) que teria sido construída entre 1914 e 1919. 
Os trabalhos para uma nova classe de couraçados que sucederia a Classe Tegetthoff
 e substituir a antiga Classe Monarch de navios de defesa costeira começaram em meados de 1911. 
 O vice-almirante Anton Haus, o Comandante da Marinha, 
 conseguiu aprovar em abril de 1914 um programa de expansão naval com o apoio do Conselho Imperial 
 austríaco e da Dieta húngara, 
garantindo assim o orçamento necessário para a construção de quatro novos couraçados dreadnought. """

palavras = texto.split()
res = Counter(palavras)
print(palavras)
print(Counter(palavras))

#Encontrando as 5 palavras com mais ocorrencia no texto - sem loop for
print(res.most_common(5))

