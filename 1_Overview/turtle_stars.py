import turtle as t

t.speed(2)

count = 0
t.bgcolor("#00e0e0")
t.color("#0000ff")
while( True ):
    t.fd(200)
    t.right(140)
    count+=1
    curpos = t.pos()
    
    if (int(curpos[0])==0 and int(curpos[1])==0 ):
        break
print( count )
input()
