def dispcont(filename, enc):
    print("\n\n==================================\n{}\n================================".format(filename))
    fs = open(filename, "rt", encoding=enc )
    txt = fs.read()
    fs.close()
    print("contents:[\n{}]".format(txt))
    print("size:{}".format(len(txt)))

    fs = open(filename, "rb" )
    bin = fs.read()
    fs.close()
    print("contents:[", end="")
    print(bin, "]")
    print("size:{}".format(len(bin)))
   

file_utf8 = "6_File_and_Data_format/txt_utf8.txt"
file_gbk = "6_File_and_Data_format/txt_gbk.txt"
file_unicode = "6_File_and_Data_format/txt_unicode.txt"

dispcont( file_utf8, "utf-8")

dispcont( file_unicode, "utf-16")

dispcont( file_gbk, "gbk")

