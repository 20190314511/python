import random as r
import time

print("开始猜数")

stopguess = False
counter = 0
timestart = time.process_time()

while stopguess==False:
    rand = r.randint(1000,10000)

    while True:
        guess=int(input("请输入猜测的四位数："))
        counter += 1
        timeend = time.process_time()

        if guess==rand:
            print("共猜测%d次，用时%d秒。"%(counter, timeend-timestart))
            cont = input("继续猜测？").lower()
            if cont.rfind("no")>=0:
                stopguess = True
            break
        else:
            guessbk = guess
            randbk = rand
            A = 0
            B = 0
            for i in range(4):
                gbits = guessbk%10
                rbits = randbk%10
                guessbk = guessbk/10
                randbk = randbk/10
                if (gbits==rbits):
                    A+=1
                else:
                    if str(rand).rfind(str(gbits))>0:
                        B+=1
            print("results: %1dA%1dB"%(A,B))
            continue
    

