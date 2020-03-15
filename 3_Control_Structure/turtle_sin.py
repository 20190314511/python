import turtle as t
import math

t.goto(300,0)
t.goto(-300,0)
t.penup()
t.goto(0,-300)
t.pendown()
t.goto(0,300)

t.penup()

width = 400
x0 = -int(width/2)
A = 200

t.goto(-width/2, 0)
t.pendown()

deltapi = 3.1415926*2/width

for i in range(width+1):
    x = i+x0
    y = A*math.sin(deltapi*x)
    t.goto(x,y)
    #print(i)

print(x,y)
input("")