from operator import le
from re import T
from tkinter import PIESLICE
import turtle as t
from unicodedata import name

#삼각형 그리기
t.color("red")
t.pensize(3)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

t.up()

#사각형 그리기
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
 
t.down()

t.bgcolor("skyblue")

# 원 그리기 
t.begin_fill()
t.circle(50)
t.fillcolor("black")
t.end_fill()

for x in range(10):
    print("7^2 =", 7**2)


import turtle as t
n = 50
t.bgcolor("black")
t.color("green")
t.speed(0)
for x in range(n):
    t.circle(80)
    t.left(360/n)

name = input("Your Name?")
print("Hello", name)

a=3

if a != 2:
    print(name)

def funsun():
    print("hi")

print(funsun())