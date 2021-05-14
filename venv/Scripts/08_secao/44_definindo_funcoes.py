'''

DEFININDO FUNÇÕES

Funções são pequenas parte de codigo trechos de códigos que realizam tarefa especifica
pode ou não receber entradas de dados e retornar uma saida de dados
muito util para executar procedimentos similares por repetidas vezes

obs. se você escrever uma função que executa varias tarefas
é bom fazer uma verificação para que ela seja simplificada


-- evita ficar reescrevendo códigos, cria uma vez e vai chamando dentro do codigo

Já utilizamos varios funções:
print, len, max, min, count, sum e muitas outras


# exemplo de utilização de função

cores = ['verde', 'amarelo', 'azul', 'branco']
nome = 'Pedro Araujo'
# usando a função integrada(bult-in) do python print()

print(cores)
print(nome)

cores.append('roxo')

print(cores)

cores.clear()
print(cores)

# DRY - Don't Repeat Yourself

# Como definir funções

Em Python a forma geral de definir função é
def nome_da_funcao(parametros_de_entrada_1, entrada_de_dados_2):
    bloco_da_funcao


onde:
nome_da_função = tem que ter letras minusculas e separadas por underscore
parametros_de_entrada  = eles são opcionais, se mais de um separar por virgula
bloco da função = também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não o retorno da função

obs.: veja que para definir uma função utilizamos a palavra reservada 'def'
infomando ao Python que estamos definindo uma função.
Tambem abrimos o codigo de codigos com os dois pontos (:). Isso é utilizado em Python para definir códigos

#Definindo a primeira função

def diz_oi():
    print('Oi!')

# Obs.:
# 1. Observe que dentro das funções podemos utilizar outras funções
# # 2. Veja que a função só executa uma tarefa
# # 3. Veja que a função não recebe parametro de entrada
# 4. Veja que a função não retorna nada

# Utilizando funções - Chamada de execução

diz_oi()

# Obs.: Nunca esqueça de utilizar o parenteses ao executar uma função

for n in range(5):
    diz_oi()

# Em Python podemos criar variaveis do tipo de uma função e executar esta função atraves da variavel
--Não é usual
oi = diz_oi
oi()


'''


def diz_oi():
    print('Oi!')

print(diz_oi())