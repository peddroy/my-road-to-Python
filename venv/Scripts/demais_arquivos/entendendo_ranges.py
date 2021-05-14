# for num in range(2, 11):
#     print(f'ramalelomante {num}')
#
# for num in range(2, 15, 2):
#     print(num)
#
# for num in range(10, 0, -1):
#     print(num)

# WHILE
#
# num = 1
#
# while num < 10:
#     print(num)
#     num = num + 1

resp = ''

while resp != 'sim':
    resp = input('Terminou Jéssica? ')

# BREAK

for num in range (1, 10):
    if num == 6:
        break
    else:
        print(num)
print('sai do loop')

while True:
    comando = input('Digite sair para sair: ')
    if comando == 'sair':
        break
