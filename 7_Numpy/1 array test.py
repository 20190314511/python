import numpy as np

a = list(range(100))
print(a)

b = np.array(a)

print(b)

c = [[ i for i in range(10)] for i in range(10)]
print(c)

d = np.array(c)
print(d)

# 每行不独立，共享一行空间
a = [i for i in range(10)]
e = [a for i in range(10)]
e[0][1] = 10
print(e)

# 每行独立，形成真正的二维数组
f = np.array(e)
f[0][2] = 20
print(f)
print(f.ndim)
print(f.shape)
print(f.size)
print(f.dtype, f.itemsize)
print(f.flags)
print(f.data)

g=f.reshape(5,20)
print(g)
print(g.ndim)
print(g.shape)


