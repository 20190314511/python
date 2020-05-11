def printms(ms):
    dim = len(ms)
    for i in range(dim):
        linesum = 0
        for j in range(dim):
            print( "{:4d} ".format(ms[i][j]), end="")
            linesum += ms[i][j]
        print( "  ", linesum)

    print()
    for i in range(dim):
        rowsum = 0
        for j in range(dim):
            rowsum += ms[j][i]
        print( "{:4d} ".format(rowsum), end="")
    print()

    main_diagonal = 0
    sub_diagonal = 0
    for i in range(dim):
        main_diagonal += ms[i][i]
        sub_diagonal += ms[i][dim-1-i]
    print("\nmain diagonal sum:%d \nsub diagonal sum:%d"%(main_diagonal, sub_diagonal))

def ms_odd(ms):
    dim = len(ms)
    x = 0
    y = int(dim/2)
    n = 1
    total = dim*dim

    while n<=total:
        ms[x][y]=n

        n+=1

        newy = (y + 1)%dim
        newx = (x - 1)%dim
        if (ms[newx][newy]>0):
            x = (x+1)%dim
        else:
            x = newx
            y = newy
        
def ms_even_even(ms):
    dim = len(ms)

    # step 1
    for i in range(dim):
        for j in range(dim):
            ms[i][j]=i*dim + j+1

    printms(ms)

    # step 2
    halfdim = int(dim/2)
    dim_1 = dim -1
    a = ms
    for i in range(halfdim):
        for j in range(halfdim):
            if (i+j)%2==0:
                a[i][j],a[dim_1-i][dim_1-j] = a[dim_1-i][dim_1-j],a[i][j]
    for i in range(halfdim):
        for j in range(halfdim,dim):
            if (i+j)%2==1:
                a[i][j],a[dim_1-i][dim_1-j] = a[dim_1-i][dim_1-j],a[i][j]

def ms_even_odd_trans(t, ms, starti, startj, startn, halfdim ):
    dim = len(ms)
    halfdim = int(dim/2)

    for i in range(starti, starti+halfdim):
        for j in range(startj, startj+halfdim):
            ms[i][j] = t[i-starti][j-startj]+startn

def ms_even_odd(ms):
    dim = len(ms)
    halfdim = int(dim/2)
    m = int((dim-2)/4)

    # step 1
    t = [[0 for i in range(halfdim)] for i in range(halfdim)]
    ms_odd(t)

    ms_even_odd_trans(t, ms, 0, 0, 1,halfdim)                               #A
    ms_even_odd_trans(t, ms, halfdim,halfdim, halfdim*halfdim+1,halfdim)    #B
    ms_even_odd_trans(t, ms, 0, halfdim, halfdim*halfdim*2+1,halfdim)       #C
    ms_even_odd_trans(t, ms, halfdim, 0, halfdim*halfdim*3+1,halfdim)       #D

    printms(ms)

    # step 2
    #	A<->D
    for i in range(halfdim):
        for j in range(m):
            if (i==m):
                offset = m
            else:
                offset = 0
            ms[i][j+offset], ms[i+halfdim][j+offset] = ms[i+halfdim][j+offset],ms[i][j+offset]
	
	# B<->C
    for i in range(halfdim):
        for j in range(m-1):
            ms[i][dim-1-j], ms[i+halfdim][dim-1-j] = ms[i+halfdim][dim-1-j],ms[i][dim-1-j]

n = 7

ms = [[0 for i in range(n)] for i in range(n)]

if n%4==0:
    ms_even_even(ms)
else:
    if n%2==0:
        ms_even_odd(ms)
    else:
        ms_odd(ms)
printms(ms)

