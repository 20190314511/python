import jieba

txt = open("5_Complex_Data_Types/threekingdoms.txt", "r").read().lower()

words = jieba.lcut(txt)

counters = {}

for word in words:
#    if word in ["，","。", "：","、","；","？","！","\"","\n"]:
#        continue
    if len(word)<=1:
        continue
    counters[word] = counters.get(word, 0)+1

items = list(counters.items())
items.sort( key=lambda x: x[1], reverse = True )

print( len(words), len(items) )
for i in range(100):
    print(items[i])