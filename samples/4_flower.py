for i in range(100,1000):
    sum = 0
    data = i
    for j in range(3):
        bits = data%10
        data = data // 10
        sum += pow(bits,3)
    if sum==i:
        print(i,end=' ')
print("")

