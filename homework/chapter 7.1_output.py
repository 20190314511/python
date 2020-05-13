import keyword

def readfile( FILENAME ):
    TXT = open(FILENAME,"r", encoding="utf-8").read()
    return TXT

def writefile( FILENAME, SOURCE ):
    NOEXT = FILENAME.strip(".py")
    NEWFILENAME = NOEXT+"_output"+".py"

    FO = open(NEWFILENAME, "w", encoding="utf-8")
    FO.write(SOURCE)
    FO.close()

def word_process( CH, WD, KWLIST, PREFIX_DOT, LAST ):
    FUNCTIONWORDS = '('

    if (WD not in KWLIST):
        if CH not in FUNCTIONWORDS and LAST==False and not PREFIX_DOT:
            WD = WD.upper()
    return WD

def parse( SOURCE ):
    STOPWORDS = "\t\n\r: ()=."
    LASTAVAILABLE = ['from', 'import']
    KWLIST = keyword.kwlist
    KWLIST.append("encoding")

    WORD = []
    OUTPUT = ""
    LAST = False
    INSTR = False
    LASTCH = ""
    PREFIX_DOT = False

    for CH in SOURCE:
        if (CH in "\"\'" or INSTR):
            WD = "".join(WORD)
            WD = word_process(CH, WD, KWLIST, PREFIX_DOT, LAST)
            OUTPUT+= WD + CH
            WORD = []
            if (LASTCH!="\\" and CH in "\"\'"):
                INSTR = not INSTR
        else:            
            if CH in STOPWORDS:
                WD = "".join(WORD)
                if (LAST==True):
                    KWLIST.append(WD.strip())
                WD = word_process(CH, WD, KWLIST, PREFIX_DOT, LAST)

                if WD in LASTAVAILABLE:
                    LAST = True
                else:
                    LAST = False
                OUTPUT += WD
                OUTPUT += CH
                WORD = []
                if (CH=="."):
                    PREFIX_DOT = True
                else:
                    PREFIX_DOT = False
            else:
                WORD.append(CH)
        if (LASTCH=='\\' and CH=="\\"):
            LASTCH = ""
        else:
            LASTCH = CH
    return OUTPUT

FILENAME = "homework/chapter 7.1.py"
TXT = readfile(FILENAME)
NEWTXT = parse(TXT)

writefile(FILENAME, NEWTXT)