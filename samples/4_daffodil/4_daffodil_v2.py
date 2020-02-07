import math
import time
import sys

# 准备pow数组，p[i][j]保存pow(i,j)
p = []
item = []
for i in range(10):
    item = []
    for j in range(10):
        item.append( pow(i,j) )
    p.append(item)

start = time.time()

index = 9
a = [0,1,2,3,4,5,6,7,8,9]

for a[index] in range(1,10):  # index
    for a[index-1] in range(10):      #index -1
        for a[index-2] in range(10):      #index -2
            for a[index-3] in range(10):      #index -3
                for a[index-4] in range(10):      #index -4
                    for a[index-5] in range(10):      #index -5
                        for a[index-6] in range(10):      #index -6
                            for a[index-7] in range(10):      #index -7
                                for a[index-8] in range(10):      #index -8
                                    sum1 = 0
                                    sum2 = 0
                                    for i in range(9,0,-1):
                                        sum1 += p[a[i]][9]
                                        sum2 = a[i]+sum2*10
                                    if (sum1==sum2):
                                        print(sum1)
                print(sum2, end='\r')
                sys.stdout.flush()



end = time.time()
print("\ttime used:%s"%(end-start))


