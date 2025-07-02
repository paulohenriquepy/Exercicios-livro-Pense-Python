# Projeto de interface

import turtle

# Desenhando um quadrado linha a linha

'''bob = turtle.Turtle()

bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

turtle.mainloop()'''

# Desenhando um quadrado usando um loop for

'''bob = turtle.Turtle()

for i in range(4):
    bob.fd(100)
    bob.lt(90)

turtle.mainloop()'''

# Escreva uma função que desenhe um quadrado

'''def square(t):

    t = turtle.Turtle()

    for i in range(4):
        t.fd(100)
        t.lt(90)

    turtle.mainloop()

square('bob')'''

# Adicionando outro parâmetro à função

def square(t, length):

    t = turtle.Turtle()

    for i in range(4):
        t.fd(length)
        t.lt(90)

    turtle.mainloop()


# Criando uma função genérica polígono

def polygon(t, length, n):

    angulo = 360 / n

    for i in range(n):
        t.fd(length)
        t.lt(angulo)

# Criando uma função chamada circle

import math

'''def circle(t, r):


    circunference = 2 * math.pi * r
    n = int(r * 2)
    length = circunference / n

    polygon(t, length= length, n = n)'''

# Criando uma versão mais geral de circle, chamada arc
# que receba um parâmetro adicional de ângulo

# Minha versão de arc
def arc(t, r, angle):


    # Converter graus em radianos
    angulo_em_radianos = angle * (math.pi / 180)

    # Criar uma variável chamada arco
    arco = angulo_em_radianos * r

    n = int(arco * 2)

    length = arco/n

    for i in range(n):
        t.fd(length)
        t.lt(angle/n)

# Versão de arc do livro

def arc_livro(t, r, angle):

    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
    
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

#######
# Criando um objeto de turtle fora das funções
#######

t = turtle.Turtle()

arc_livro(t, 50, 180)

# Fazer o programa parar apenas uma vez, depois de executar tudo
turtle.mainloop()


