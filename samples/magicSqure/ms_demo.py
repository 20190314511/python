def print_ms(ms):
    n = len(ms)
    for i in range(n):
        linesum = 0
        for j in range(n):
            linesum+=ms[i][j]
            print("{:3d}".format(ms[i][j]), end=" ")
        print("  {}".format(linesum) )

def ms_odd(ms):
    n = len(ms)

    x=0
    y=int(n/2)

    for i in range(1, n*n+1):
        ms[x][y] = i

        newx = (x - 1)%n
        newy = (y+1)%n
        if ms[newx][newy]>0:
            x = (x+1)%n
        else:
            x = newx
            y = newy


n = 7

#line = [0 for i in range(n)]
ms = [[0 for i in range(n)] for i in range(n)]

ms_odd(ms)

print_ms(ms)

