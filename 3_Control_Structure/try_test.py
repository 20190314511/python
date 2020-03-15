# 测试try语句

a = input("input a number:")

try:
    i = int(a)
except ValueError:
    print("value error")
    i = -1
else:
    print("no error")
finally:
    print("don't care if error, finally print")

print(i)
