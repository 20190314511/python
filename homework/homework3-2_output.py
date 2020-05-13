SUM = 0
COUNT = 0
for I in range(1,101):
    if (I%3==0 or I%5==0 or I%7==0):
        COUNT +=1
        SUM += I
print("SUM=%d, COUNT=%d, AVG=%.2f"%(SUM,COUNT, SUM/COUNT) )
