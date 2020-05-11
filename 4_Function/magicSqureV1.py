def printSquare(a):
    global count

    count +=1
    print("========%d========"%count)
    for i in range(3):
        print(a[i*3:i*3+3], end="\n")
    print()


def exam(a):
    if a[0]+a[1]+a[2]==a[3]+a[4]+a[5]==a[6]+a[7]+a[8]:
        if a[0]+a[3]+a[6]==a[1]+a[4]+a[7]==a[2]+a[5]+a[8]:
            if a[0]+a[8]==a[2]+a[6]:
                return True
    return False

def ms(a,level):

    if (level==9):
        if exam(a):
            printSquare(a)
        return

    for a[level] in range(1,10):
        if level>0 and a[level] in a[0:level]:
            continue
        ms(a, level+1)


a = [0]*9
count = 0
ms(a, 0)

