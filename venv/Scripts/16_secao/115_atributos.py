'''

POO - ATRIBUTOS

Atributos representam as caracteristicas do objeto. ou seja, pelos atributos nos
conseguimos representar computacionalmente os estados de um objeto

Em Python dividimos os atribuitos em três grupos

1. Atributos de Instancia
2. Atributos de Classes
3. Atributos Dinâmicos

# 1. Atributos de instancia
São atributos dentro do metodo construtor
obs. metodo construtor é um metodo especial utilizado para a construção do objeto

em java uma classe lampada, incluindo seus atributos ficaria mais ou menos assim:

public class Lampada(){
    private int voltagem;  # primeiro declara os atributos
    private String cor;  # é private porque somente dentro da classe pode ter acesso
    private Boolean ligada = false;

    public Lampada (int voltagem, String cor){  # construtor do Java
        this.voltagem = voltagem;
        this.cor = cor;
    }

    public int getVoltagem(){  #exemplo... necessário fazer para outros atributos
        return this.voltagem;
    }
}


Atributos Publicos e Atributos Privados

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é publico.
Ou seja, pode ser acessado em todo o projeto. 
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado,
ou seja, que deve ser acessado/utilizado somente dentro da propria classe onde está
declarado utiliza-se __ duplo underscore no inicio de seu nome
Isso é conhecido como Name Mangling


# classes com Atributos de instancias publicos


class Lampada:

    def __init__(self, voltagem, cor):  # metodo construtor em Python com a declaração dos atributos
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):  # função dentro da classe é chamada de método
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# self = é o objeto que está executando o metodo. o proprio objeto executando o metodo

# Atributos Públicos e Atributos Privados


class Acesso:

    def __init__(self, email, senha):
        self.email = email  # Marcação __ de atributo privado
        self.__senha = senha

    def mostra_senha(self):  # metodo que acessa o atributo dentro da própria classe
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python
# não vai impedir que façamos acesso aos atributos sinalizados como Privados
# fora da classe.

# Exemplo:


user = Acesso('user@gmailcom', '123456')

print(user.email)

# print(user.__senha)  # AttributeError

# Name Mangling - Temos acesso ao atributo privado, mas não deveriamos
print(user._Acesso__senha)

user.mostra_senha()

user.mostra_email()

# O que significa Atributos de instancia?
# Significa que ao criarmos instancias/objetos de uma classe, todas a instancias
# terão estes atributos

user1 = Acesso('user1@gmail.com', 'senhalegal')
user2 = Acesso('user2@gmail.com', 'outrapassword')

user1.mostra_email()
user2.mostra_email()


# ATRIBUTOS DE CLASSE

# O que significa Atributos de classes?

# Atributos de classe são atributos declarados diretamente na classe, ou seja,
# fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado
# entre todas as instancias da classe. Ou seja, ao inves de cada instancia da classe
# ter seus proprios valores como é o caso dos atributos de instancia, com atributos de
# classe todas as instancias terão o mesmo valor para este atributo


# Refatorar classe produto

class Produto:

    # Atributo de Classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0  # Atributo de classe

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        # aqui está atualizando o valor do contador, passando o id como contador
        Produto.contador = self.id


p1 = Produto('Play', 'video mais', 2350)  # instancia criada
p2 = Produto('Shampoo', 'cosmético', 14.00)  # instancia criada

# Não é a forma correta, pois não preciso criar uma instancia pra acessar um atributo de classe
print(p1.imposto)
# Não é a forma correta, pois não preciso criar uma instancia pra acessar um atributo de classe
print(p2.imposto)
print(p1.valor)
print(p2.valor)

# Obs. Não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)  # Acesso correto

print(p1.id)
print(p2.id)


# Em linguagens como Java, os atributos de classe aqui em Python são chamados de
# atributos estáticos

'''


# ATRIBUTOS DINÂMICOS (não é comum)

# É um atributo de instancia que pode ser criado em tempo de execução
# O atributo dinâmico será exclusivo da instancia que o criou


class Produto:

    # Atributo de Classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0  # Atributo de classe

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        # aqui está atualizando o valor do contador, passando o id como contador
        Produto.contador = self.id


p1 = Produto('play', 'eletronico', 1234)
p2 = Produto('alho', 'alimento', 19)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'  # note que na classe produto não existe o atributo peso

print(
    f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor},  Peso: {p2.peso}')

# print(
# f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor},  Peso: {p1.peso}')  # AttributeError


# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

del p2.peso

print(p2.__dict__)  # após a deleção do atributo dinâmico peso

del p2.descricao

print(p2.__dict__)  # após a deleção do atributo dinâmico peso
