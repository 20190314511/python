import turtle as t

count = 0
while( True ):
    t.fd(200)
    t.right(140)
    count+=1
    curpos = t.pos()
    
    if (int(curpos[0])==0 and int(curpos[1])==0 ):
        break
print( count )
input()
