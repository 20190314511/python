#GovRptWordCloudv1.py
import jieba
import wordcloud
f = open("samples/实例12-政府工作报告词云源代码/新时代中国特色社会主义.txt", "r", encoding="utf-8")

t = f.read()
f.close()
ls = jieba.lcut(t)

txt = " ".join(ls)
w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc"    
    )
w.generate(txt)
w.to_file("samples/实例12-政府工作报告词云源代码/chinamapT1.jpg")


