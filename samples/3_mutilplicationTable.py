def printRow(i):
    for j in range(1,i+1):
        print("%d*%d=%-2d"%(j,i,i*j), end="  ")
    print("")

def printTable():
    for i in range(1,10):
        printRow(i)


printTable()

