import matplotlib.pyplot as plt
import numpy as np

# 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
plt.figure(figsize=(8, 6), dpi=80)

# 再创建一个规格为 1 x 1 的子图
plt.subplot(111)

x = np.linspace(-2, 6, 50)
y1 = x + 3        # 曲线 y1
y2 = 3 - x        # 曲线 y2
y3 = 4*np.sin(x) + 5

# 绘制颜色为蓝色、宽度为 1 像素的连续曲线 y1
plt.plot(x, y1, color="blue", linewidth=1.0, linestyle="-")
# 绘制颜色为紫色、宽度为 2 像素的不连续曲线 y2
plt.plot(x, y2, color="#800080", linewidth=1.0, linestyle="--")
plt.plot(x, y3, color="#808080", linewidth=2.0, linestyle="-")

# 设置横轴的上下限
plt.xlim(-1, 6)
# 设置纵轴的上下限
plt.ylim(-2, 10)

plt.show()