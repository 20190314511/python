def main():
    n=eval(input("请输入阶数："))
    drawsq(n)

def drawsq(n):
    line=5*n
    for i in range(line+1):
        if i%5==0:
            print(n*"+----",end="")
            print("+")
        else:
            print ("|    "*n,end="")
            print("|")

