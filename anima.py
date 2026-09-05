import turtle as t

janela = t.Screen()
janela.setup(width=800, height=600)
janela.title("Uma mensagem especial")
janela.bgcolor("#170b1f")

caneta = t.Turtle()
caneta.color("#ff4f87")
caneta.fillcolor("#ff4f87")
caneta.speed(3)

caneta.begin_fill()
caneta.left(140)
caneta.forward(180)
caneta.circle(-90, 200)
caneta.left(120)
caneta.circle(-90, 200) 
caneta.forward(180)
caneta.end_fill()

caneta.hideturtle()

estrelas = t.Turtle()
estrelas.shape("circle")
estrelas.color("#fff2b2")
estrelas.penup()
estrelas.shapesize(0.15)

posicoes = [
    (-280, 180),
    (-210, 100),
    (260, 170),
    (220, 60),
    (-300, -80),
    (280, -130),
    (-150, -190),
    (150, -200),
]

for x, y in posicoes:
    estrelas.goto(x, y)
    estrelas.stamp()

estrelas.hideturtle()

caneta.goto(0, -180)
caneta.color("white")
caneta.write(
    "Para você",
    align="center",
    font=("Arial", 20, "bold")
)

janela.mainloop()