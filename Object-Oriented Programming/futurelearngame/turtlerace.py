from turtle import Turtle
from random import randint
#*Typical for classes to be capitalize
#*Just some stuff using the turtle module.
suguru = Turtle()
suguru.color("red")
suguru.shape("turtle")

suguru.penup()
suguru.goto(-160, 100)
suguru.pendown()

akashi = Turtle()
akashi.color("green")
akashi.shape("turtle")

akashi.penup()
akashi.goto(-160, 80)
akashi.pendown()

keiko = Turtle()
keiko.color("yellow")
keiko.shape("turtle")

keiko.penup()
keiko.goto(-160, 60)
keiko.pendown()

kailash = Turtle()
kailash.color("black")
kailash.shape("turtle")

kailash.penup()
kailash.goto(-160, 40)
kailash.pendown()

for i in range(100):
    suguru.forward(randint(1,5))
    akashi.forward(randint(1,5))
    keiko.forward(randint(1,5))
    kailash.forward(randint(1,5))