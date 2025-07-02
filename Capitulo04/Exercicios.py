# Exercício 4.2
# Desenhar flores usando o Turtle

import math
import turtle

#### O primeiro exercício era o desenho de flores

def arco(t, r, angle):


    # Converter graus em radianos
    angulo_em_radianos = angle * (math.pi / 180)

    # Criar uma variável chamada arco
    arco = angulo_em_radianos * r

    n = int(arco/3) + 1

    length = arco/n


    for i in range(n):
        t.forward(length)
        t.left(angle/n)


def petala(t, r, angle):

    '''Executa a função arco duas vezes, produzindo arcos espelhados'''

    for _ in range(2):
        arco(t, r, angle)
        t.left(180 - angle)



def flor(t, r, angle, n_petalas):

    '''Executa a função pétala várias vezes'''

    for i in range(n_petalas):
        petala(t, r, angle)
        # A flor só fica completa se o ângulo abaixo for múltiplo de 360
        t.left(360/n_petalas)

####
# O segundo exercícios são polígonos formados por triângulos
####



def poligonos(t, comprimento, numero_de_lados):

    angulo = 360 / numero_de_lados

    for i in range(numero_de_lados):
        t.forward(comprimento)
        t.backward(comprimento)
        t.left(angulo)

    '''t.forward(comprimento)
    t.left(180 - angulo)


    for i in range(numero_de_lados):
        t.forward(2 * comprimento * math.sin(math.pi / numero_de_lados))
        t.left(angulo)'''



# Espiral de Arquimedes

def raios(t, comprimento, numero_de_lados = 8):

    angulo = 360 / numero_de_lados

    t.penup()
    t.left(90)
    t.forward(13)
    t.pendown()
    for i in range(numero_de_lados):
        t.forward(comprimento)
        t.backward(comprimento)
        t.left(angulo)


def circulos_concentricos(t, raio):

    for i in range(9):
        t.circle(i * raio)
        t.penup()
        t.setposition(0, -(i * raio))
        t.pendown()

def circulos_com_raios(t, comprimento, raio, numero_de_lados = 8):

    raios(t, comprimento, numero_de_lados= 8)
    t.penup()
    t.setheading(0)  # apontar para a direita
    t.goto(0, -raio)
    t.pendown()
    circulos_concentricos(t, raio)

#######
# Criando um objeto de turtle fora das funções
#######

t = turtle.Turtle()

circulos_com_raios(t, 104, raio = 13)

# Fazer o programa parar apenas uma vez, depois de executar tudo
turtle.mainloop()
