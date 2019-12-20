lines = 10

for i in range(lines):
    for j in range(lines-i):
        print(" ", end="")
    for j in range(i*2+1):
        print("*",end="")
    print("")

for i in range(lines, -1, -1):
    for j in range(lines-i):
        print(" ", end="")
    for j in range(i*2+1):
        print("*",end="")
    print("")
