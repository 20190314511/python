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

print(12345*54321)

# 输入/输出测试
pie = 3.14159
r = float(input("r="))
print( 's=%.2f, l=%.2f' % (r*r*pie, 2*pie*r) )

# 循环及换行测试
for i in range(10):
    print(i,end="")
    if (i+1)%4==0:
        print()
        
# 循环
for i in range(100):
    print("sqrt(%2d)=%5.3f"%(i,math.sqrt(i) ), end="  " )
    if (i+1)%4==0:
        print()
