'''

LISTAS ANINHADAS (NESTED LISTS)

Em algumas linguagem existem estruturas de dados chamadas arrays:
- Arrays unidimensionais (arrays/vetores)
- Arrays multidimensionais (matrizes)

Em Python tem-se listas

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for lista in listas:
    print(lista)

for lista in listas:
    for numero in lista:
        print(numero)

[[print(numero) for numero in lista] for lista in listas]


'''

# Gerando tabuleiro 3x3

tabuleiro = [[valor for valor in range(1, 4)] for numero in range(1, 4)]
print(tabuleiro)

# Gerando jogo da velha
velha = [['X' if valor % 2 == 0 else 'O' for valor in range(1, 4)] for numero in range(1, 4)]
print(velha)

