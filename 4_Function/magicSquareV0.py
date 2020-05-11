def exam(a):
    if a[0]+a[1]+a[2]==a[3]+a[4]+a[5]==a[6]+a[7]+a[8]:
        if a[0]+a[3]+a[6]==a[1]+a[4]+a[7]==a[2]+a[5]+a[8]:
            if a[0]+a[8]==a[2]+a[6]:
                return True
    return False

def myprint(a, count):
    print("======={}=======".format(count))
    for i in range(3):
        print(a[i*3:i*3+3], end="\n")
    print()

a = [0]*9
count = 0
for a[0] in range(1,10):
    for a[1] in range(1,10):
        if a[1]==a[0]:
            continue
        for a[2] in range(1,10):
            if a[2] in a[0:2]:
                continue
            for a[3] in range(1,10):
                if a[3] in a[0:3]:
                    continue
                for a[4] in range(1,10):
                    if a[4] in a[0:4]:
                        continue
                    for a[5] in range(1,10):
                        if a[5] in a[0:5]:
                            continue
                        for a[6] in range(1,10):
                            if a[6] in a[0:6]:
                                continue
                            for a[7] in range(1,10):
                                if a[7] in a[0:7]:
                                    continue
                                for a[8] in range(1,10):
                                    if a[8] in a[0:8]:
                                        continue

                                    if exam(a)==True:
                                        count += 1
                                        myprint(a,count)

                                                
                                    
