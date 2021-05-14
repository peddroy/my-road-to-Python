n = int(input('Digite o valor a ser sacado: '))

print(n)

notas = 100, 50, 20, 10, 5, 2, 1

for valores in notas:
    quantidade_notas = n // valores
    n = n - quantidade_notas * valores
    print(f'Quantidade de notas de {valores}: {quantidade_notas}')
