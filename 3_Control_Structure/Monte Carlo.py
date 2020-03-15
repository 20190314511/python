import random
import math
import time

count = 0
total = 10000000

start = time.time()

for i in range(total):
    x,y = random.random(), random.random()
    if x*x+y*y<=1.0:
        count +=1

print( time.time()- start, count/total*4.0 )

