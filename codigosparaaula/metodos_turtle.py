import turtle
janela = turtle.Screen()
janela.bgcolor("red")
tata = turtle.Turtle()
tata.color("yellow")
tata.shape("turtle")

print(range(5,60,2))
tata.penup()                    # isso é novo
for size in range(5,60,2):      # começar com size = 5 e passo 2
    tata.stamp()                # deixar um carimbo no canvas
    tata.forward(size)          # vá para frente
    tata.right(24)              # vire 24 graus a direita

janela.exitonclick()
