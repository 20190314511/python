
def th(head, interval, tail, hr):
    print(head,end="")
    print(hr*(4-1),end="")
    for i in range(10):
        print(interval+hr*7,end="")
    print(tail)

# ━┏ ┓ ┳ ┗ ┛ ┻ ╋ ┃ ┣ ┫ ┻ 制表符
vc="┃"

th("┏","┳","┓","━")

print("{} \\ {}".format(vc,vc), end="")
for a in range(10):
    print(" {:^6.1f}{}".format(a*0.1,vc),end='') 
print()

th("┣","╋","┫","━")

for value in range(11):
    print("{} ".format(vc), end="")
    print("{:-2d}{} ".format(value,vc),end='')
    for a in range(10):
        sqrt=(value+a*0.1)**0.5
        print("%-6.3f%c "%(sqrt,vc),end='')
    print()

th("┗","┻","┛","━")
