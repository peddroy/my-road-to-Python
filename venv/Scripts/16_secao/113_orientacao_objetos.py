'''

PROGRAMAÇÃO ORIENTADA A OBJETOS

É um paradigma de programação que utiliza o mapeamento 
de objetos do mundo real para modelos computacionais 
    
Paradigmas:

1. estruturada
2. orientação a objetos
3. funcional

Na orientação a objetos temos os principais elementos:

1. classe - modelo do objeto do mundo real sendo representado computacionalmente
2. atributos (das classes) - caracteristicas do objeto
3. metodos (função) - comportamento do objeto -  metodos está dentro de uma classe - função dentro da classe é metodo
4. construtor - metodo especial utilizado para criar os objetos - é metodo especial - utilizado para criar objetos a partir da classe
5. objeto - instancia da classe - os elementos criados a partir da classe são objetos ou instancias


'''


numero = 10
print(numero)
print(type(numero))

nome = 'Geek'
print(nome)
print(type(nome))


class Produto:
    pass


ps4 = Produto()  # Aqui está o construtor da classe produto. ps4 é um objeto da classe produto

print(ps4)
print(type(ps4))
