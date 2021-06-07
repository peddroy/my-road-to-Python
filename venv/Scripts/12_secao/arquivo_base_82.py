def soma_impares(numeros):
    total = 0
    for i in numeros:
        if i % 2 != 0:
            total = total + i
    return total


if __name__ == '__main__':
    lista = [1, 3, 6, 9]

    tupla = 1, 2, 4, 8

    cidades = [('Berlin', 29), ('Tokyo', 18), ('New York', -4), ('Deli', 40),
               ('Curitiba', 19), ('Santos', 28), ('Manaus', 32)]

    def c_para_f(cidades): return (cidades[0], (9/5) * cidades[1] + 32)

    print('macarão com queijo')

else:
    print('O bagulho é loco')
