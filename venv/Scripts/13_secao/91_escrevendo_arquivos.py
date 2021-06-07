'''

ESCREVENDO EM ARQUIVOS

1 - Primeiro precisamos abrir o arquivo

o open() abre como default o arquivo pra consulta

obs. Ao abrir um arquivo pára leitura, não podermos realizar a escrita nele.
Apenas ler!
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo.
Apenas escrever nele!

o Modo w é de write

Ao abrir um arquivo para escrita,
o arquivo é criado no sistema

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write
Esta função recebe uma string como parametro, caso contrario teremos um TypeError

Abrindo um arquivo para escrita com modo w, se o arquivo não existir será criado
caso ele ja existe, o anterior sera apagado e um novo será criado.
Todo o arquivo anterior será perdido

# Forma Pythonica de escrever

with open('novotexto.txt', 'w') as arquivo:
    arquivo.write('Vamos cagando e andando.\n')
    arquivo.write('Tá muito com isso aqui\n')
    arquivo.write('Vou fechando por aqui.')


# Forma tradicional de escrita em arquivo

arquivo = open('novotexto.txt', 'w')

arquivo.write('nowww!\n')
arquivo.write('Gloryy\n')
arquivo.write('Come on!!')

with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)


'''

with open('newtxt.txt', 'w') as arquivo:
    while True:
        fruta = input('Digite uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta
            arquivo.write('\n')
        else:
            break
