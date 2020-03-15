# 演示三角形打印的计算问题

n = eval(input("底边边长："))

if (1<n<21):
    for i in range(1,n+1):
        print("*"*i, end="  ")
        for j in range( n - i ):
            print(" "*2, end="")
        print("* "*i,end="")
        print()
else:
    print("请输入2~20之间的数字")
    