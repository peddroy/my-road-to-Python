'''
LEN, ABS, SUM, ROUND

len() - retorna o tamanho do iteravel
print(len([1, 2, 3, 4]))

print(len({1, 3, 5}))


# Por debaixo dos panos o Python faz o seguinte
# Dunder Len (__len__())
print('Pedro Araujo'.__len__())


abs() - retorna o valor absoluto de um numero inteiro ou real

print(abs(-5))
print(abs(-3.14))

# sum() - recebe como parametro um iteravel, podendo ter um valor inicial,  
# e retorna a soma de todos os elementos

print(sum({1, 2, 6}))
print(sum({'a': 1, 'b': 2, 'c': 3}.values()))
print(sum([1, 2, 3]))
print(sum([1, 2, 3], 5))

round() - retorna um numero arredondado para n digito de precisão 
após a casa decimal. 
Se a precisão não for informada retorna o inteiro mais proximo da entrada

print(round(10.2))
print(round(10.8))
print(round(15.342453533, 2))

'''
