sum = 0
count = 0
for i in range(1,101):
    if (i%3==0 or i%5==0 or i%7==0):
        count +=1
        sum += i
print("sum=%d, count=%d, avg=%.2f"%(sum,count, sum/count) )
