'''

ANY E ALL

all() - retorna True se todos os elementos do iteravel é verdadeiro ou se o iteravel está vazio
any() - returna True se qualquer elemento do iteravel é verdadeiro. Se estiver vazio retorna False
'''

# Exemplo all()

# print(all([0 , 1 , 2 , 3 , 4 , 5])) # todos os elementos (lista) são verdadeiros? Não!
# print(all([1 , 1 , 2 , 3 , 4 , 5])) # todos os elementos (lista) são verdadeiros? Sim!
# print(all([])) # todos os elementos (lista) são verdadeiros? Sim!
# print(all({1, 'a', 1.2})) # todos os elementos (set) são verdadeiros? Sim!
# print(all(['Marcus Aguiar'])) # todos os elementos (string) são verdadeiros? Sim!

# nomes = ['Carla', 'Cristina', 'Cibely']
#
# print(all(nome[0] == 'C' for nome in nomes))
#
# print(all(letra for letra in 'aei' if letra in 'aeiou')) # confuso - se vazio retorna True
#

print(all([num for num in [1 , 7 , 5 , 9 , 11] if num % 2 == 0])) # essas porra de exemplo sempre dão True

print(any([num for num in [1, 5, 2] if num % 2 == 0])) # retorna True pq tem um elemento True
print(f'aqui {any([])}')
print(f'aqui outro {any([0, 1])}')
print(any([num for num in [1, 5, 3] if num % 2 == 0])) # retorna False pq tem um elemento False
print(any([num for num in [] if num % 2 == 0])) # retorna False pq é uma lista vazia

print(f' naice {any([num for num in [1, 0, 3] if num % 2 == 0])}')







