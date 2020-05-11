a = "dddd ad  "
print(len(a), len(a.strip()))

fs = open("5_Complex_Data_Types/hamlet.txt","r")

txt = fs.readlines(43)

sum = 0
for t in txt:
    sum += len(t)

fs.close()

print(txt, sum)
