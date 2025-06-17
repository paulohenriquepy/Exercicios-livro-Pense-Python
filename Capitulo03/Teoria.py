# Capitulo 3 - Funções

#print(int('32'))

#print(float('24.5'))

#print(str(32.5))

import math

# Converter senos em radianos
graus = 45
radianos = graus / 180 * math.pi

# Calcula o seno de radianos
#print(math.sin(radianos))

# Definindo uma função


# Usando uma função dentro de outra função

def imprimir_refrao():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


def repetir_refrao():
    imprimir_refrao()
    imprimir_refrao()

# Não precisa criar uma variável para armazenar o resultado
# A função não retorna nada ainda
repetir_refrao()


# Parâmetros e argumentos

def imprimir_duas_vezes(palavra):
    print(palavra)
    print(palavra)

# Se o argumento for um string, precisa vir entre aspas
imprimir_duas_vezes('Spam')

# A função funciona com qualquer argumento
imprimir_duas_vezes(math.pi)

# Podemos usar qualquer tipo de expressão como argumento
imprimir_duas_vezes('Spam ' * 4)

# Vamos imprimir duas vezes o cosseno de pi
imprimir_duas_vezes(math.cos(math.pi))

# Podemos usar uma variável como um argumento
nome = 'Paulo'
imprimir_duas_vezes(nome)

# As variáveis e os parâmetros são locais
def juntar_duas_vezes(parte1, parte2):

    juntar = parte1 + parte2
    imprimir_duas_vezes(juntar)

linha1 = 'Underererê, dererê, dererê. '
linha2 = 'Unbadabadá, badabá, dabauê.'

juntar_duas_vezes(linha1, linha2)

