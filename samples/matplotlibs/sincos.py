# -*- coding: UTF-8 -*-
# By Yohanna: Finished in 2017/7/21
# Have a nice weekend
import numpy as np
import matplotlib.pyplot as plt

# Create a new figure of size 8*6 point, using 100 dots per inch
plt.figure(figsize=(8,6), dpi=80)

# 1*1的子图
plt.subplot(111)

# 生成出图的原始数据
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

# cos的plot, 蓝色实线（线宽=2）&& sin的Plot, 绿色实线 （线宽=2）
# 并添加图例
plt.plot(X, C, color="purple", linewidth=2.0, linestyle="-",label="Cosine")
plt.plot(X, S, color="black", linewidth=2.0,linestyle="-" ,label="Sine")
plt.legend(loc='upper left',frameon=True)

# 标记兴趣点并添加标签
t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)],color="pink",linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),],50, color="purple")
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t,t],[0,np.sin(t)],color="blue",linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),],50, color="black")
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# 设置X，Y 轴的范围
plt.xlim(X.min()*1.1, X.max()*1.1)
plt.ylim(C.min()*1.1, C.max()*1.1)

# 标记X，Y轴。注意:这里使用了Latex（to allow for nice rendering of the label）
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1],
           [r'$-1$', r'$0$', r'$+1$'])

# 移动X，Y坐标轴(例如，坐标轴居中，显示四个象限)
# 由于坐标轴包含四个(top/bottom/left/right), 将top和right坐标轴颜色设为none;
ax = plt.gca() #gca() Get Current Axes; gcf() Get Current Figure.
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 移动bottom和left至数据空间的coordinate 0
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# 增强横纵坐标标签的可读性
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(14)
    label.set_bbox(dict(facecolor="white",edgecolor="None", alpha=0.7))
#  显示结果
plt.show()