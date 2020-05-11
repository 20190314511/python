import jieba

seg_list = jieba.cut("我来到北京清华大学")

print(seg_list)


print("全模式: " + "-".join(seg_list))  # 全模式
print()
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("精准模式: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("我来到北京清华大学")
print("默认模式: " + "/ ".join(seg_list)) 


seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print("cut_for_search:\n"+ ", ".join(seg_list))

seg_list = jieba.lcut("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", cut_all=True)  # 搜索引擎模式
print("lcut:\n"+ ", ".join(seg_list))
print(seg_list)