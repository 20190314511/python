import datetime as dt
    
mscount=0
total = 0
dtlast = dt.datetime.now()
dtstart = dtlast

n = 4
nn = n*n

result = [0]*nn
remain = [1]*(nn+1)

ssum = 0
for i in range(0,nn):
    ssum += (i+1)
ssum = ssum / n

filename = str(n)+"x"+str(n)+ " result("+ dtstart.strftime('%y%m%d-%H%M%S') + ").txt"

def exam(n):
    global ssum
    diagsum = 0
    adiagsum = 0

    base = 0
    for i in range(0,n):
        diagsum += result[base+i]
        if (diagsum>ssum):
            return 0
        adiagsum += result[(n-i-1)+base]
        if (adiagsum>ssum):
            return 0
        base += n
    
    if (diagsum!=ssum or adiagsum!=ssum) :
        return 0
    
    return 1


def examPart( r,c, n, rowSum, colSum, threshold_max, threshold_min):

    ''' 部分行求和'''
    partSum = rowSum
    if (partSum + threshold_max[n-1-c]<ssum or partSum + threshold_min[n-1-c]>ssum):
        return 0

    partSum = colSum
    if (partSum + threshold_max[n-1-r]<ssum or partSum + threshold_min[n-1-r]>ssum):
        return 0

    return 1


def myprint():
    global total, n, filename,mscount
    global result, dtlast, dtstart

    #fp = open(filename,'a')

    dtnow = dt.datetime.now()
    dtsep = dtnow - dtlast
    dtlast = dtnow

    #print("%-8d %-8d %8.2f %6.2f"%(total, mscount, (dtnow-dtstart).total_seconds(), dtsep.total_seconds() ), file=fp)
    print("%-8d %-8d %8.2f %6.2f"%(total, mscount, (dtnow-dtstart).total_seconds(), dtsep.total_seconds() ) ) #result)
    '''for i in range(0,n):
        for j in range(0,n):
            print("%5s%2d"%("", result[i*n+j]), end=' ', file=fp)
        print(file=fp)
    '''
    #fp.close()

def calc_threshold( n, threshold_max, threshold_min ):
    global remain, nn

    k = 0
    #threshold_min[0]=0
    for i in range (1,nn+1):
        if (remain[i]==0):
            continue
        k+=1
        threshold_min[k]=i+threshold_min[k-1]
        if (k==n-1):
            break
    #if (k<n-1):
    #    for i in range(k+1, n):
    #        threshold_min[i] = threshold_min[k]

    k = 0
    #threshold_max[0]=0
    for i in range(nn, 0, -1):
        if (remain[i]==0):
            continue
        k+=1
        threshold_max[k]=i+threshold_max[k-1]
        if (k==n-1):
            break
    #if (k<n-1):
    #    for i in range(k+1, n):
    #        threshold_max[i] = threshold_max[k]

def magicSqure( level, n, rowSum, colSum ):
    global mscount, total
    global result
    global nn,remain
    
    threshold_max = [0]*n
    threshold_min = [0]*n

    r = int( (level-1)/n )
    c = (level-1)%n

    calc_threshold( n, threshold_max, threshold_min )

    if (c==0):
        rowSum=0

    for i in range (1, nn+1):
        if (rowSum+i>ssum or colSum[c]+i>ssum):
            break
        if (i in result) :
            continue
            
        result[level-1]=i
        rowSum +=i
        colSum[c] +=i
        remain[i]=0

        if (examPart( r, c , n, rowSum, colSum[c], threshold_max, threshold_min )==1):
            if ( level==nn ):
                mscount=mscount+1
                if (exam(n)==1):
                    total +=1
                    myprint()
            else:
                magicSqure( level+1, n, rowSum, colSum)
        remain[result[level-1]]=1
        rowSum -=i
        colSum[c] -=i
        result[level-1]=0

fp = open(filename,'w')
fp.close()

rowSum = 0
colSum = [0]*n
magicSqure(1, n, rowSum, colSum )
print(mscount, total)
