
def th(head, interval, tail, hr):
    print(head,end="")
    print(hr*(4-1),end="")
    for i in range(10):
        print(interval+hr*7,end="")
    print(tail)
    return

# ━┏ ┓ ┳ ┗ ┛ ┻ ╋ ┃ ┣ ┫ ┻ 制表符
vc="┃"

th("┏","┳","┓","━")

# 打印标题行
print("{} \\ {}".format(vc,vc), end="")
for col in range(10):
    print(" {:^6.1f}{}".format(col*0.1,vc),end='') 
print()

th("┣","╋","┫","━")

# 打印表格行
for row in range(11):
    print("{} ".format(vc), end="")
    print("{:-2d}{} ".format(row,vc),end='')
    for col in range(10):
        sqrt=(row+col*0.1)**0.5
        print("%-6.3f%c "%(sqrt,vc),end='')
    print()

th("┗","┻","┛","━")
