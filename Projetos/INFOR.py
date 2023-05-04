from turtle import *
from time import sleep
draw = Turtle()
draw.pensize(20)
#draw.color("Blue")

draw.pu()
draw.goto(-220,0)
draw.pd()

#I
draw.fd(50)
draw.bk(100)
draw.fd(50)
draw.lt(90)
draw.fd(100)
draw.rt(90)
draw.fd(50)
draw.bk(100)

#Próxima letra, não pode usar o goto() pq não dá para saber a distância de draw

draw.pu()
draw.fd(50)
draw.rt(90)
draw.fd(100)
draw.lt(90)
draw.fd(90)
draw.pd()

#N
draw.lt(90)
draw.fd(100)
draw.rt(147)
draw.fd(118)
draw.lt(147)
draw.fd(100)

#Espaçamento

draw.pu()
draw.lt(180)
draw.fd(100)
draw.lt(90)
draw.fd(40)
draw.lt(90)
draw.pd()

#F
draw.fd(100)
draw.rt(90)
draw.fd(60)
draw.bk(60)
draw.rt(90)
draw.fd(50)
draw.lt(90)
draw.fd(40)

#Espaçamento entre outra letra
draw.pu()
draw.bk(40)
draw.rt(90)
draw.fd(50)
draw.lt(90)
draw.fd(130)
draw.pd()

#O
draw.circle(50)

#Espaçamento
draw.pu()
draw.fd(90)
draw.pd()

#R
draw.lt(90)
draw.fd(100)
draw.rt(90):
draw.fd(30)
draw.circle(-30,180)
draw.fd(30)
draw.rt(180)
draw.fd(30)
draw.rt(60)
draw.fd(44)

#♡
draw.pu()
draw.seth(0) #Retorna a posição Leste, podia se substituído por: #draw.home()
draw.goto(0,-500)
draw.pd()
draw.color("Blue")
draw.begin_fill()
draw.pensize(3)
draw.left(50)
draw.fd (270)
draw.circle(100,200)
draw.rt(140)
draw.circle(100,200)
draw.goto(0,-500) #Uso do draw.goto() pq não se sabe a distância do semicírculo até o ponto
#draw.fd (215)
draw.end_fill()

#♡
draw.pu()
draw.seth(0)
draw.goto(-200,350)
draw.pd()
draw.color("Red")
draw.begin_fill()
draw.lt(80)
draw.fd (133)
draw.circle(50,200)
draw.rt (140)
draw.circle(50,200)
draw.fd (133)
draw.end_fill()

#♡
draw.pu()
draw.seth(0)
draw.goto(200,350)
draw.pd()
draw.color("Red")
draw.begin_fill()
draw.lt(20)
draw.fd (133)
draw.circle(50,200)
draw.rt (140)
draw.circle(50,200)
draw.fd (133)
draw.end_fill()

#texto
draw.pu()
draw.goto(-350,-650)
draw.color("blue")
draw.pd()
draw.write ("Infor do coração♡, já que não posso ir para Desenvolvimento de Sistema :(", move = False , align = 'left' , font = ('Arial', 5, 'normal') )

#</3
sleep(10)
draw.pu()
draw.goto(0,-500)
draw.color('white')
draw.seth(0)
draw.pensize(15)
draw.pd()
draw.lt(100)
draw.fd(100)
draw.rt(60)
draw.fd(70)
draw.lt(80)
draw.fd(100)
draw.rt(70)
draw.fd(60)
draw.lt(70)
draw.fd(50)

#clean
draw.pu()
draw.goto(-350,-650)
draw.pd()
draw.seth(0)
draw.color("white")
draw.begin_fill()
for i in range(0,2):
    draw.fd(800)
    draw.lt(90)
    draw.fd(100)
    draw.lt(90)
draw.end_fill()

#txt
draw.pu()
draw.goto(-350,-650)
draw.color("blue")
draw.pd()
draw.write ("Quem eu quero enganar, tô muito triste ;(", move = False , align = 'left' , font = ('Arial', 5, 'normal') )

mainloop()