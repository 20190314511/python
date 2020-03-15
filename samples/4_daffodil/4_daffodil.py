import math
import time
import sys

# 准备pow数组，p[i][j]保存pow(i,j)
p = []
for i in range(10):
    item = []
    for j in range(10):
        item.append( pow(i,j) )
    p.append(item)

start = time.time()

for bits_count in range(3,10):
    loopstart = pow(10, bits_count-1)
    loopend = pow(10, bits_count)
    
    for i in range(loopstart, loopend):
        sum = 0
        data = i
        while(data>0):
            bits = data%10
            data = data // 10
            sum += p[bits][bits_count]
        if sum==i:
            print(i,end=' ')
            sys.stdout.flush()
    end = time.time()
    print("\ttime used:%s"%(end-start))


