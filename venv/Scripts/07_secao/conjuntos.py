'''

CONJUNTOS

Conjunto em qualquer linguagem de programação, estamos fazendo referencia à Teoria dos Conjuntos da Matemática

Em Python os conjuntos são chamados de Sets

Da mesma forma que na Matemática
Sets - Não possuem valores duplicados
Sets - Não possuem valores ordenados
Sets - Não são indexados
    Elementos não são acessados via indice

Conjuntos são bons para se utilizar quando precisamos armazenar dados
mas não nos importamos com a ordenação deles,
quanto não precisamos nos preocupar com chave/valor e itens duplicados

Os conjuntos em Python são referenciados com chaves {}.

Diferença entre Sets e Dictionary
- Dicionário tem chave/valor
- Conjunto tem apenas valor

# Definindo um conjunto

#Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) #Aqui temos valor repetido

print(s)
print(type(s))

#ao criar um conjunto caso seja adicionado um caso ja exisite o mesmo será ignorado e não fara parte do conjunto
#sem gerar erros


# Forma 2 - Mais comum

#obs.: pode-se misturar tipos de dados em sets

receita = {
    'jan', 'fev', 'mar', 'mar', 1, 7, 1, 7, True
}

print(receita)
print(type(receita))

#Converter string, listas, tuplas em set
#Elimina os duplicados

meunome = 'Pedro Araujo'

meunome = set(meunome)
print(meunome)
print(type(meunome))

meunomeemset = set('Pedro Araujo')
print(type(meunomeemset))
print(meunomeemset)

# Lista em set

minhalista = [1, 2 ,3 ,4 ,5 ,6, 6, 6, 6]
print(minhalista)
print(type(minhalista))

minhalistaemset = set(minhalista)
print(minhalistaemset)
print(type(minhalistaemset))

# Tupla em set

minhatupla = 1, 2, 1, 4, 5, 1

print(minhatupla)
print(type(minhatupla))

minhatuplaemset = set(minhatupla)
print(minhatuplaemset)
print(type(minhatuplaemset))

print(set(minhatupla)) #fazendo conversar no print

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem 3')
else:
    print('Não tem 3')


#Importante: Além de não duplicar, não tem ordem

dados = '99, 2, 5, 73, 72, 7, 4, 4, 5, 99, 45'

lista = [99, 2, 5, 73, 72, 7, 4, 4, 5, 99, 45]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = 99, 2, 5, 73, 72, 7, 4, 4, 5, 99, 45
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# não aceita chaves duplicadas
dicionario = {}.fromkeys([99, 2, 5, 73, 72, 7, 4, 4, 5, 99, 45], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# não aceita elementos duplicados
conjunto = {99, 2, 5, 73, 72, 7, 4, 4, 5, 99, 45}
print(f'Set {conjunto} com {len(conjunto)} elementos')


# Podemos iterar em sets

s = {1, 3, 7, 7, 8, 9, 4}

for valor in s:
    print(valor)


# Usos interessantes em sets

# Situação
# Imagina que temos que fazer um formulário para um museu
# Os visitantes chegam e preenchem de ql cidade vieram
# Teremos que adicionar esse dado em uma lista (pode haver duplicados)

cidades = ['São Paulo', 'Atibaia', 'Bragança', 'Atibaia', 'Perdões', 'Atibaia', 'Perdões']

print(cidades)
print(f'Quantidade de pessoas: {len(cidades)} visitantes')

# Quantas cidades únicas temos?
print(f'As quantidade de cidades distintas é: {len(set(cidades))}')


# Adicionar elementos

s = {1, 2, 3}
print(s)
s.add(4)
s.add(4) #duplicidade não gera erro. apenas ignora
print(s)

# Remover elementos
# Forma 1

s.remove(3) #não é indice é o proprio valor
print(s)

# obs.: no remove caso o valor não for encontrado será gerado KeyError

# Forma 2

s.discard(1)
print(s)

#obs.: no discard, caso o valor não for encontrado não será gerado erro, será ignorado



# Copiando um conjunto para outro

s = {1, 2, 3, 4}
print(s)

# Forma 1 - DeepCopy - totalmente separados e independentes

novoconjunto = s.copy()
print(novoconjunto)

novoconjunto.add(14)
print(s)
print(novoconjunto)


#Forma 2 - ShallowCopy - os conjuntos são relacionados

s = {11, 22, 33}

novoconjunto = s

print(s)
print(novoconjunto)

novoconjunto.add(44)

print(s)
print(novoconjunto)


# Podemos remover todos os elementos de um conjunto

s.clear()
print(s)



# METODOS MATEMÁTICOS DE CONJUNTO

# Imagine que temos dois conjuntos: Estudantes de Python e estudantes de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}

estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

#Alguns alunos estudam Python e Java

#Problema 1 - Gerar relatório com nomes de estudantes unicos

# Forma 1 - Union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando pipe |

unicos2 = estudantes_python | estudantes_java
print(unicos2)

#Problema 2 - Gerar relatório de estudando que estão em ambos cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Problema 3 - Gerar relatório de estudantes que fazem apenas um curso

# Utilizando difference

so_python = estudantes_python.difference(estudantes_java)
print(so_python)
so_java = estudantes_java.difference(estudantes_python)
print(so_java)





'''


#
# s = {1, 2, 4, 5, 7, 8}
# print(s)
#
#
# # Soma*, Maior Valor*, Menor Valor*, Tamanho
# # *inteiros e reais
#
# print(sum(s))
# print(max(s))
# print(min(s))
# print(len(s))
#

vai = 'vai'
print(vai)