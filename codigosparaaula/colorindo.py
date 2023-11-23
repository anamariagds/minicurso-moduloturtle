import turtle
jn = turtle.Screen()             # Cria uma janela e define seus atributos
jn.bgcolor("lightgreen")


tata = turtle.Turtle()           # cria e define seus atributos
tata.color("hotpink")
tata.pensize(5)

# desenha um triângulo equilátero

tata.forward(80)                 
tata.left(120)
tata.forward(80)
tata.left(120)
tata.forward(80)
tata.left(120)                   # complete o triângulo

tata.right(180)                  #  muda de direção
tata.forward(80)                 # se move para longe da origem



jn.exitonclick()