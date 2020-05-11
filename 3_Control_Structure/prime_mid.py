import time
import math

# function   m=a*b
def isprime( m ):
    stop = int(math.sqrt(m))+1
    for i in range(2,stop):
        if (m%i==0):
            retval = False
            break
    else:
        retval = True

    return retval   

######################################################################
# main 
count = 0
start = time.time()
scope = 1000000
for n in range(2,scope):
    if isprime(n)==True:
        #print("{}".format(n), end=" ")    
        count +=1
    if (n%10000==0):
        print("{:4.0f}%".format(n/scope*100), end="\r")

print("\n{}, 用时：{}".format(count, time.time()-start))

