def hannon(n, source, destination, temp):
    if (n==1):
        move(n, source, destination)
    else:
        hannon(n-1, source, temp, destination)
        move(n, source, destination)
        hannon(n-1, temp, destination, source)

def move(n, source, destination):
    global  count

    count +=1
    print(count, "  ", n, "  ", source, "---->", destination, sep="")

count = 0
try:
    n = eval(input("input a integer:"))
    if type(n)==int:
        hannon(n, "A", "C", "B")
except:
    print("input a number")


