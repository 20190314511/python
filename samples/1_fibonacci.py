a = 1
b = 1
count = 2
print( "%-25d %-25d"%(a,b), end=" ")

for i in range(100):
    t = a+b
    a = b
    b = t
    count += 1
    print("%-25d"%(t), end=" ")
    if count%5 == 0:
        print("")

