import time

scale = 40
print("start")
for i in range(scale+1):
    a = "*"*i
    b = "."*(scale-i)
    c = i/scale*100
    print("{:^3.0f}%[{}->{}]".format(c, a, b), end="\r")
    time.sleep(0.1)
print("\nend")
