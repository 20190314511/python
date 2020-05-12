import re
import sys


txt = open("5_Complex_Data_Types/hamlet.txt", "r").read().lower()

pa = re.compile("[^a-zA-Z0-9]")
newtxt = re.sub(pa, " ", txt)

words = newtxt.split()

counters = {}

for word in words:
    t = word    #.strip()
    counters[t] = counters.get(t, 0)+1

items = list(counters.items())
items.sort( key=lambda x:x[1], reverse = True )

for i in range( 20 ):
    t = items[i][0]
    print(items[i])

fs = open("5_Complex_Data_Types/hamlet_words.txt","wt")
for item in items:
    fs.writelines( item[0] + "("+ str(item[1])+")\n" )
fs.close()

