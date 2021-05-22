'''
RAISE

Lança excessões

Não é uma função é uma palavra reservada com def e outras.

É util para criamos nossas proprias exceções e mensagens de erro

A forma geral de utilização é:

raise TipodeErro('mensagem de erro')

'''


def colore(texto, cor):
    cores = ['verde', 'amarelo', 'azul', 'branco']
    if type(texto) is not str:
        raise TypeError("Texto precisa ser string")
    elif type(cor) is not str:
        raise TypeError("cor precisa ser string")
    elif cor not in cores:
        raise ValueError(f"a cor precisa ser uma entre {cores}")
    print(f'o {texto} será impresso na cor {cor}')


colore('inxála', 'roxo')
