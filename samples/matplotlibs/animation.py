# -*- coding: UTF-8 -*-
# By Yohanna: Finished in 2017/7/21
# Have a nice weekend
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 首先要创建一个空白图纸,并且建立新的axis,1:1的aspect ratio
fig = plt.figure(figsize=(6,6), facecolor='pink')
ax = fig.add_axes([0,0,1,1],frameon=False, aspect=1)

# 使用散点图scatter来创建rings,以此作为雨滴
# 首先明确雨滴的数目和大小
n = 50
size_min =50
size_max = 50*50
# 其次要明确雨滴的位置
P = np.random.uniform(0,1,(n,2))
# 雨滴的颜色,color channel 从0（transparent）到1（opaque）
C = np.ones((n,4))*(0,0,0,1)
C[:,3] = np.linspace(0,1,n)
# 圈的大小
S = np.linspace(size_min, size_max, n)

# 散点图绘制
scat = ax.scatter(P[:,0], P[:,1], s = S, lw = 0.5,
                  edgecolors = C, facecolors = 'None')
# Ensure limits are [0,1] and remove ticks
ax.set_xlim(0,1), ax.set_xticks([])
ax.set_ylim(0,1), ax.set_yticks([])

# 接下来是定义动图的update function
def update(frame):
    global P, C, S

    # 每个雨滴 都要产生透明渐变的效果
    S += (size_max - size_min)/n
    # 对特定雨滴进行复位（re-use the ring to set a new ring）
    i = frame % 50
    P[i] = np.random.uniform(0,1,2)
    S[i] = size_min
    C[i,3] = 1

    # 更新所有的离散点
    scat.set_edgecolors(C)
    scat.set_sizes(S)
    scat.set_offsets(P)

    # 返回到修改后的对象上
    return scat,

# 最后使用matplotlib的 FuncAnimation生成动图
animation = FuncAnimation(fig, update, interval=10, blit=True, frames=200)
plt.show()