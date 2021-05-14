'''
GENERATOR EXPRESSION

Em aulas passadas nós estudamos:
- List comprehensions
- Dict comprehensions
- Set comprehensions

Não vimos:
- Tuple comprehensions, isso porque elas se chamam Generators

Generator é mais performático do que Listcomprehension
List comprehension gera uma lista que fica na memória




nomes = ['Carla', 'Cristina', 'Carlos', 'Champion', 'Caio']

print(any([nome[0] == 'C' for nome in nomes]))

# Poderiamos ter feito do seguinte modo

print(any(nome[0] == 'C' for nome in nomes))

res1 = [nome[0] == 'C' for nome in nomes]
res2 = (nome[0] == 'C' for nome in nomes)

print(type(res1))
print(res1)
print(type(res2))
print(res2)


from sys import getsizeof

# Pra que serve getsizeof? Retorna a quantidade de bytes em memória do elemento passado como parametro

#  Aqui mostra quantos bytes a string 'Geek' está ocupando em memória
print(getsizeof('geek'))

print(getsizeof([x * 10 for x in range(1000)]))
print(getsizeof({x * 10 for x in range(1000)}))
print(getsizeof({x: x * 10 for x in range(1000)}))
print(getsizeof(x * 10 for x in range(1000)))


'''

nomes = ['Carla', 'Carlos', 'Caio', 'Cibely', 'Vanessa']

res = all(nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

mas = map(lambda r: r, [nome[0] == 'C' for nome in nomes])
print(type(mas))
print(tuple(mas))

fil = list(filter(lambda r: r[0] == 'C', [nome for nome in nomes]))
print(fil)

maps = list(map(lambda r: r[0] == 'C', [nome for nome in nomes]))
print(maps)
