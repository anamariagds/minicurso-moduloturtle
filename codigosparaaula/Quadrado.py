import turtle            # permite usar as funções e objetos do módulo turtle
s = turtle.Screen()    # cria uma janela gráfica
t = turtle.Turtle()   # cria um turtle chamado alex


for i in [0,1,2,3]:      # repita 4 vezes
    t.forward(50)
    t.left(90)

s.exitonclick()