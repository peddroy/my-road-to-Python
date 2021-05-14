'''

SET COMPREHENSION

não repete
não é ordenado

'''

numeros = {num for num in range(5)}
print(numeros)

numeros = {num ** 2 for num in range(10)}
print(numeros)

# Faça uma alteração para gerar dicionário ao inves de set

numeros = {num: num ** 2 for num in range(10)}
print(numeros)

letras = {letra for letra in 'Geek University'}
print(letras)


