print('%-4s'%("\\"),end='')
for a in range(10):
    print("%-8.1f"%((a-1)*0.1),end='') 

print()
for value in range(11):
    print("%-4d"%(value),end='')
    for a in range(10):
        sqrt=(value+a*0.1)**0.5
        print("%-8.3f"%(sqrt),end='')
    print()

