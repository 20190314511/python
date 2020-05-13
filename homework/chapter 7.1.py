import keyword

def readfile( filename ):
    txt = open(filename,"r", encoding="utf-8").read()
    return txt

def writefile( filename, source ):
    noext = filename.strip(".py")
    newfilename = noext+"_output"+".py"

    fo = open(newfilename, "w", encoding="utf-8")
    fo.write(source)
    fo.close()

def word_process( ch, wd, kwlist, prefix_dot, last ):
    functionwords = '('

    if (wd not in kwlist):
        if ch not in functionwords and last==False and not prefix_dot:
            wd = wd.upper()
    return wd

def parse( source ):
    stopwords = "\t\n\r: ()=."
    lastAvailable = ['from', 'import']
    kwlist = keyword.kwlist
    kwlist.append("encoding")

    word = []
    output = ""
    last = False
    instr = False
    lastch = ""
    prefix_dot = False

    for ch in source:
        if (ch in "\"\'" or instr):
            wd = "".join(word)
            wd = word_process(ch, wd, kwlist, prefix_dot, last)
            output+= wd + ch
            word = []
            if (lastch!="\\" and ch in "\"\'"):
                instr = not instr
        else:            
            if ch in stopwords:
                wd = "".join(word)
                if (last==True):
                    kwlist.append(wd.strip())
                wd = word_process(ch, wd, kwlist, prefix_dot, last)

                if wd in lastAvailable:
                    last = True
                else:
                    last = False
                output += wd
                output += ch
                word = []
                if (ch=="."):
                    prefix_dot = True
                else:
                    prefix_dot = False
            else:
                word.append(ch)
        if (lastch=='\\' and ch=="\\"):
            lastch = ""
        else:
            lastch = ch
    return output

filename = "homework/chapter 7.1.py"
txt = readfile(filename)
newtxt = parse(txt)

writefile(filename, newtxt)