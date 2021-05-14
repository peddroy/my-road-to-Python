'''

MODO COLLECTIONS - DEQUE

Podemos dizer que o deque é uma lista de lta performance





'''

# Realizar importação

from collections import deque

#criando deques

deq = deque('geek')

print(deq)

#add elementos

deq.append('y') #add no final da lista

print(deq)

deq.appendleft('x') #add no começo da lista

print(deq)

# remover elementos

print(deq.pop()) #remove e retorna o removido (final lista)
print(deq)

print(deq.popleft()) #remove e retorno o removido (começo lista)
print(deq)

# help(deque)

deq.insert(2, 'alpha')
print(deq)

deq.reverse()
print(deq)
