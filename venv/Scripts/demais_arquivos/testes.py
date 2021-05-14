
'''
def row_sum_odd_numbers(n):
    lista = []
    i = 1
    while i <= n:
        if i == n:
            for linha in range(1, i+1):
                lista.append(linha)
        else:
            i += 1

    soma = sum(lista)
    return soma


print(row_sum_odd_numbers(12))

'''

n = 13

for i in range(1, n):
    for j in range(1, i + 1):
        # print(i)
        if j % 2 != 0:
            print(f'{j}', end='')
    print()
