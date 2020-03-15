import time
import math

def isprime(n):
    stop = int(math.sqrt(n))+1

    for i in range(3, stop,2):
        if (n%i==0):
            break
    else:
        return True
    return False

def progress( ratio ):
    scale = 40
    i = int(ratio * scale)
    a = "*" * i
    b = "."*(scale-i)
    c = ratio*100
    print("{:^4.1f}%[{}->{}]".format(c, a, b), end="\r")    


start = time.time()
count = 1
max = 10000000
processcount = 0
for i in range(3,max,2):
    processcount += 1
    if isprime(i)==True:
        count +=1
        #print(i, end=" ")
    if processcount>5000:
        processcount = 0
        progress(i/max)
print(max, count, time.time() - start, end=" "*30)

