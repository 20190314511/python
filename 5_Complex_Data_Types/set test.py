txt = open("5_Complex_Data_Types/hamlet.txt", "r").read().lower()

for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
    txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格

words = txt.split()

counters = {}

for word in words:
    t = word    #.strip()
    counters[t] = counters.get(t, 0)+1

items = list(counters.items())
items.sort( key=lambda x: x[1], reverse = True )

print( len(words), len(items) )
for i in range(10):
    print(items[i])

