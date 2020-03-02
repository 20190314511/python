# Tim Peter  Zen of Python

import this
import math

# single line comment 汉字测试
"""
多行注释
汉字注释
"""

# 输出演示
print("Hello, Wrold!")
print("你好！")
print("你好！", "世界", sep='', end='!\n')

print("*****", end="\n\n")

print(12345*54321)      # 默认回车\n
print()                 # 仅打印回车

# 输入/输出测试
pie = 3.14159
r = float(input("r="))      # 根据需要转换数据类型
print( 's=%.2f, l=%.2f' % (r*r*pie, 2*pie*r) )

# eval函数测试
eval("print(3,3)")
eval("print(10*r)")     # eval表达式中可以包含变量
a = eval("pow(3,3)")
print(type(a), a)
b = eval("'3'+'4'*4")
print(type(b),b)
print("eval(\"3+4\")=", a)
print()

# 循环及换行测试
for i in range(1:10):
    print(i,end="")
    if (i+1)%4==0:
        print()
        
# 循环计算平方根，演示print格式串的复杂用法
for i in range(100):
    print("sqrt(%2d)=%5.3f"%(i,math.sqrt(i) ), end="  " )
    if (i+1)%4==0:
        print()
