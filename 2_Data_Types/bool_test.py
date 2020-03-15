
# 相当于 25>2 and 2>1
print( "25>2>1\t\t:{}".format(25>2>1) )

# 先对(25>2)进行处理，结果为true，对应值为1， 1 > 1 返回false
print( "(25>2)>1\t:{}".format((25>2)>1) )

# and运算符总是返回第二个操作数
print( "5 and 6\t\t:{}".format(5 and 6) )
print( "6 and 5\t\t:{}".format(6 and 5) )

# 按顺序运算，6 and 5 返回5， 后边or操作可以忽略
print( "6 and 5 or 4\t:{}".format(6 and 5 or 4) )

# or运算符总是返回第一个非0操作数，后续操作忽略
print( 3 or 2 )
print( 2 or 3 )

# 理解并掌握逻辑运算
print( 2 or 3 and 4 or 5 )
print( 0 or 3 and 0 or 5 )
print( 0 or 3 and 1 or 5 )

print( )