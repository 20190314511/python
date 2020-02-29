n = int(input("请输入数字n："))
str = "Hello World!1"

if n==0:
    print(str)
elif n>0:
    for c in str:
        print(c)
else:
    if (len(str)%2!=0):
        str = str+" "
    for i in range(0,len(str), 2):
        print(str[i],str[i+1],sep="")
        
