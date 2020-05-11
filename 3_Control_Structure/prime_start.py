import time
import math

def isprime(m):
    stop = int(math.sqrt(m)) +1
    for i in range(2,stop):
        if (m%i==0):
            return False
    return True

def printBar( p ):
    scale = 40
    i = int( p *scale )
    a = "*"*i
    b = "."*(scale-i)
    c = p*100
    print("{:^3.0f}%[{}->{}]\r".format(c, a, b), end="")    

##########################################

scope = 1000000
count = 0

start = time.time()

for n in range(2,scope):
    if isprime(n)==True:
        count+=1
    if n%1000==0:
        printBar( n/scope )

print(count, time.time()-start )

