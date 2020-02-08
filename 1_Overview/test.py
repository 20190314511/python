def judge(randstr, guessstr):
    rbits=[]
    gbits=[]
    A=0
    B=0

    # 将字符串拆为单字符数组，便于后续比较
    for c in randstr:
        rbits.append(c)
    for c in guessstr:
        gbits.append(c)

    # 处理猜对位数，并将各位清孔
    for i in range( len(gbits) ):
        if gbits[i]==rbits[i]:
            A+=1
            gbits[i]="A"
            rbits[i]="A"

    # 将猜对的位数去除
    if A>0:
        for i in range( gbits.count("A") ):
            gbits.remove("A")
            rbits.remove("A")        
        randstr = ""
        for j in range(len(rbits)):
            randstr += rbits[j]

    print("abcd:"+randstr)
    # 比较其余数字正确位数    
    for c in gbits:
        if c=="":
            continue
        if( randstr.rfind(c)>=0):
            B+=1
    return "A"+str(A)+"B"+str(B)  

print(judge("7758", "6758"))
