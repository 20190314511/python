import time

def printBar( p ):
    scale = 40
    i = int( p *scale )
    a = "*"*i
    b = "."*(scale-i)
    c = p*100
    print("{:^3.0f}%[{}->{}]\r".format(c, a, b), end="")    

scale = 40
print("start")
for i in range(scale+1):
    printBar( i/scale )
    time.sleep(0.5)

print("\nend")
