import random as r
import time

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

    right_char = "?"
    # 处理猜对位数，并将各位清孔
    for i in range( len(gbits) ):
        if gbits[i]==rbits[i]:
            A+=1
            gbits[i]=right_char
            rbits[i]=right_char

    # 将猜对的位数去除
    if A>0:
        for i in range( gbits.count(right_char) ):
            gbits.remove(right_char)
            rbits.remove(right_char)        
        randstr = ""
        for j in range(len(rbits)):
            randstr += rbits[j]

    # 比较其余数字正确位数    
    for c in gbits:
        if c=="":
            continue
        if( rbits.count(c)>0):
            B+=1
            rbits.remove(c)

    return "A"+str(A)+"B"+str(B)  

print("开始猜数")

stopguess = False
timestart = time.process_time_ns()

while stopguess==False:
    counter = 0
    rand = r.randint(1000,10000)

    while True:
        guess=int(input("请输入猜测的四位数："))
        counter += 1
        timeend = time.process_time_ns()

        if guess==rand:
            print("共猜测%d次，用时%d秒。"%(counter, (timeend-timestart)/1000000))
            cont = input("继续猜测？").lower()
            if cont.rfind("no")>=0:
                stopguess = True
            break
        else:
            guessbk = str(guess)
            randbk = str(rand)
            print(randbk+":"+judge(randbk, guessbk))
            continue
    

