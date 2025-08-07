import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
colors = ["red", "blue", "green", "purple", "yellow", "orange"]

for i in range(100):
    pen.color(random.choice(colors))
    pen.forward(i * 2)
    pen.right(59)

turtle.done()

a = 'sandeep is my name my name'
a
b = " ".join(word.capitalize() for word in a.split(" ")[::-1])

l = {}
for word in b.split(" "):
    if word in l:
        l[word] += 1
    else:
        l[word] = 1

