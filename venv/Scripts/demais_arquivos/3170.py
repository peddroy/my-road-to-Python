b = int(input())
g = int(input())

total_bolas = g // 2

if b < total_bolas:
    bolas_pendentes = total_bolas - b
    print(f'Faltam {bolas_pendentes} bolinha (s)')
else:
    print('Amelia tem todas as bolinhas!')
