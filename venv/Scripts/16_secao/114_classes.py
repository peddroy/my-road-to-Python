'''

POO - Classes

Classes nada mais são do que modelos dos objetos dos mundo real
sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar 
o controle das lampadas da sua casa

classes podem conterr
1. atributos - representam as caracteristicas do objeto ou seja
pelos atributos conseguimos representar computacionalmente os estados de um objeto
No caso da lampada, possivelmente iriamos querer saber se a lampada é 110 ou 220 volts,
se ela é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela e etc.


2. metodos - funções - representam os comportamentos dos objetos, ou seja, 
as ações que este objeto pode realizar no seu sistema. No caso da lampada,
por exemplo, um comportamento comum que muito provavelmente queremos representar
no nosso sistema é o de ligar e desligar a mesma.

Em Python para definir uma classe utilizamos uma palavra reservada 'class'.

Utilizamos a palavra pass quando temos um bloco de codigo que ainda não está implementado.
Obs. Quando nomeamos nossas classe em Python utilizamos por convenção o nome com inicial
maiusculo. Se o nome for composto utiliza-se todas as iniciais maiuscula, todas juntas

Dica Geek: Em computação não utilizamos: Acentuação, caracteres especiais
espaços ou similares para nomes de classes, atributos, métodos, arquivo, diretórios e etc


Quando estamos planejando um software e definimos quais classes teremos que ter no sistema,
chamamos objetos que serão mapeados para classes de entidades.

'''


class Lampada:
    pass


lamp = Lampada()

print(type(lamp))


class ContaCorrent:
    pass


class Produto:
    pass


class Usuario:
    pass
