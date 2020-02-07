import turtle as t


t.pensize(1)

count = 19
width = 380
delta = width / count

for i in range(count+1):
    t.penup()
    t.goto(-width/2, -width/2+delta*i)
    t.pendown()
    t.goto(width/2, -width/2+delta*i)
    t.penup()
    t.goto(-width/2+delta*i, -width/2)
    t.pendown()
    t.goto(-width/2+delta*i, width/2)
c=input()

