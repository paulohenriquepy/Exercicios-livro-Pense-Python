# Exercício 3.1

def justificar_a_direita(s):

    comprimento_do_string = len(s)
    numero_de_espacos = 70 - comprimento_do_string
    print(' ' * numero_de_espacos + s)

#justificar_a_direita('Paulo')

# Exercício 3.2

def imprimir_spam(valor):
    print(valor)

'''def executar_duas_vezes(f, valor):
    f(valor)
    f(valor)'''

#executar_duas_vezes(imprimir_spam, 'spam')

'''def executar_quatro_vezes(f, valor):
    executar_duas_vezes(f, valor)
    executar_duas_vezes(f, valor)'''

#executar_quatro_vezes(imprimir_spam, 'spam')


# Exercício 3.3

def do_twice(f):

    'Executa uma função duas vezes'

    f()
    f()

def do_four(f):

    'Executa uma função quatro vezes'

    do_twice(f)
    do_twice(f)

def linhas_horizontais():

    'Imprime linhas horizontais'

    print('+', '-' * 4, '+', end = ' ')
    print('-' * 4, '+')

def linhas_verticais():

    print('|', ' ' * 4, '|', end = ' ')
    print(' ' * 4, '|')

def estrutura_basica():

    'Desenha a estrutura básica'

    linhas_horizontais()
    do_four(linhas_verticais)

def figura_final():

    'Desenha a figura final'

    do_twice(estrutura_basica)
    linhas_horizontais()

#figura_final()

# Exercício final

def linhas_horizontais_duplicadas():

    'Imprime linhas horizontais duplicando a abordagem anterior'

    print('+', '-' * 4, '+', end = ' ')
    print('-' * 4, '+', end = ' ')
    print('+', '-' * 4, '+', end=' ')
    print('-' * 4, '+')


def linhas_verticais_duplicadas():

    'Imprime linhas vertificais duplicando a abordagem anterior'

    print('|', ' ' * 4, '|', end = ' ')
    print(' ' * 4, '|', end = ' ')
    print('|', ' ' * 4, '|', end=' ')
    print(' ' * 4, '|')

def estrutura_basica_duplicada():

    'Desenha a estrutura básica duplicada'

    linhas_horizontais_duplicadas()
    do_four(linhas_verticais_duplicadas)

def figura_final_duplicada():

    'Desenha a figura final duplicada'

    do_twice(estrutura_basica_duplicada)
    linhas_horizontais_duplicadas()

do_twice(figura_final_duplicada)