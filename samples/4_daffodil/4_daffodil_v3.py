import time

code = {}
for i in range(10):
    code[str(i)] = i

a = [[i for i in range(10)] for i in range(10)]

for i in range(10):
    for j in range(10):
        a[i][j] = pow(i, j)

count = 0
start = time.time()

incpower = 1000
power = 3
for i in range(100, 1000000000):
    if i%10000==0:
        print("{:4.2f}%".format(i*100/1000000000), end = "\r")
    num = str(i)
    if (i>=incpower):
        power +=1
        incpower *=10

    bitsum = 0
    for c in num:
        bitsum += a[code[c]][power]
    if bitsum==i:
        count +=1
        print(count, i, time.time()-start, "                ")


