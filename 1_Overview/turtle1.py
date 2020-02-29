import turtle as t

t.setup(800,600,100,100)
t.screensize(400,300,"#e0e0e0")
t.color("#f00000")
t.goto(100,150)


t.setup(800,600,50,50)

t.speed(10)
t.bgcolor("#f00000")
t.color("#00f000")
t.up()
t.goto(-150,-150)

t.down()
t.fd(300)
t.left(120)
t.fd(300)
t.left(120)
t.fd(300)


t.up()
t.goto(-100,100)
t.down()

t.reset()

drawing=False
count = 0
while(drawing and t.pos()==(0.0,0,0) ):
    drawing = True
    t.fd(200)
    t.right(144)
    count+=1

print( count )
input()
