import turtle
import random
def principal():
    while True:
        n = int(input('Quantos objetos? '))
        if n <= 0:
            break
        else:
            for i in range(n):
                controle = random.randint(1, 2)
                if controle == 1:
                    quadrado()
                if controle == 2:
                    circulo()

def quadrado():
    t = turtle.Turtle()
    lado = random.randint(10, 50)
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.begin_fill()
    for j in range(4):
        t.forward(lado)
        t.right(90)
    t.end_fill()

def circulo():
    t = turtle.Turtle()
    raio = random.randint(10, 50)
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.begin_fill()
    t.circle(raio)
    t.end_fill()
principal()
