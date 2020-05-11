import math

n = 125
c = 0
for i in range(5,n+1, 5):
    temp = i
    while (temp>0 and temp%5==0):
        c+=1
        temp = temp//5

print(c)
