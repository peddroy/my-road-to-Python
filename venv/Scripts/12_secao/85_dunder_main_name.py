'''

DUNDER MAIN AND DANDER NAME

Dunder = Dobble UnderScore

Dunder Main = __main__
Dunder Name = __name__

Dunder é utilizado para criar funções, atributos, propriedade 
e etc e não gerar conflito com os nomes desses elementos na programação

Na linguagem C, temos um programa da seguinte forma:

int main (){
    return 0;
}

Em Java temos um programa da seguinte forma:

public static void main(String[] args){
}

Em Python, se executarmos um módulo Python diretamente 
na linha de comando, internamente o Python atribuirá
a variavel __name__ o valor __main__ indicando que este modulo
é o modulo de execução principal

'''

import primeiro
import segundo
