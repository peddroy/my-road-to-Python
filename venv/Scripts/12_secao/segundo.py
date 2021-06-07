import primeiro


def segunda_funcao():
    return 'Retorno da Segunda Função'


if __name__ == '__main__':
    print(segunda_funcao())
else:
    print('Não executei a segunda função. Estou fora do main!')


print(primeiro.primeira_funcao())
