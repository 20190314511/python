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
            print("共猜测{:d}次，用时{:d}秒。".format(counter, timeend-timestart))
            cont = input("继续猜测？").lower()
            if cont.rfind("no")>=0:
                stopguess = True
            break
        else:
            if guess>rand:
                print("猜大了")
            else:
                print("猜小了")
            continue
    

