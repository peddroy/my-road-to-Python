n = int(input())

print(n)

if n >= 100:
    quantidadenotacem = n // 100
    resto = n % 100
    print(f'{quantidadenotacem} nota(s) de R$ 100,00')
else:
    print('0 nota(s) de R$ 100,00')

if resto >= 50:
    quantidadenotacinquenta = resto // 50
    resto = resto % 50
    print(f'{quantidadenotacinquenta} nota(s) de R$ 50,00')
else:
    print('0 nota(s) de R$ 50,00')

if resto >= 20:
    quantidadenotavinte = resto // 20
    resto = resto % 20
    print(f'{quantidadenotavinte} nota(s) de R$ 20,00')
else:
    print(f'0 nota(s) de R$ 20,00')

if resto >= 10:
    quantidadenotadez = resto // 10
    resto = resto % 10
    print(f'{quantidadenotadez} nota(s) de R$ 10,00')
else:
    print('0 nota(s) de R$ 10,00')

if resto >= 5:
    quantidadenotacinco = resto // 5
    resto = resto % 5
    print(f'{quantidadenotacinco} nota(s) de R$ 5,00')
else:
    print('0 nota(s) de R$ 5,00')

if resto >= 2:
    quantidadenotadois = resto // 2
    resto = resto % 2
    print(f'{quantidadenotadois} nota(s) de R$ 2,00')
else:
    print('0 nota(s) de R$ 2,00')

if resto >= 1:
    quantidadenotaum = resto // 1
    resto = resto % 1
    print(f'{quantidadenotaum} nota(s) de R$ 1,00')
else:
    print('0 nota(s) de R$ 1,00')
