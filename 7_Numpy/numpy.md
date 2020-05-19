# Numpy

## 1 array

### 1.1 概念
NumPy 数组的维数称为秩（rank），秩就是轴的数量，即数组的维度，一维数组的秩为 1，二维数组的秩为 2，以此类推。

在 NumPy中，每一个线性的数组称为是一个轴（axis），也就是维度（dimensions）。比如说，二维数组相当于是两个一维数组，其中第一个一维数组中每个元素又是一个一维数组。所以一维数组就是 NumPy 中的轴（axis），第一个轴相当于是底层数组，第二个轴是底层数组里的数组。而轴的数量——秩，就是数组的维数。

很多时候可以声明 axis。axis=0，表示沿着第 0 轴进行操作，即对每一列进行操作；axis=1，表示沿着第1轴进行操作，即对每一行进行操作。

NumPy 的数组中比较重要 ndarray 对象属性有：

属性| 	说明
--|--
ndarray.ndim|	秩，即轴的数量或维度的数量
ndarray.shape| 	数组的维度，对于矩阵，n 行 m 列
ndarray.size| 	数组元素的总个数，相当于 .shape 中 n*m 的值
ndarray.dtype| 	ndarray 对象的元素类型
ndarray.itemsize| 	ndarray 对象中每个元素的大小，以字节为单位
ndarray.flags| 	ndarray 对象的内存信息
ndarray.real| 	ndarray元素的实部
ndarray.imag |	ndarray 元素的虚部
ndarray.data |	包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。

### 1.2 创建空数组

* empty.empty
    ```
    numpy.empty(shape, dtype = float, order = 'C')


    import numpy as np 
    x = np.empty([3,2], dtype = int) 
    print (x)

    ```

* numpy.zeros
    ```
    numpy.zeros(shape, dtype = float, order = 'C')

    import numpy as np

    # 默认为浮点数
    x = np.zeros(5) 
    print(x)
    
    # 设置类型为整数
    y = np.zeros((5,), dtype = np.int) 
    print(y)
    
    # 自定义类型
    z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
    print(z)
    ```
* numpy.ones
使用1填充数组

### 1.3 从已有数组创建数组

* numpy.asarray

    ```
    numpy.asarray(a, dtype = None, order = None)
    ```

    参数| 	描述
    --|--
    a| 	任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组
    dtype| 	数据类型，可选
    order| 	可选，有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。

* numpy.frombuffer
    numpy.frombuffer 用于实现动态数组。
    numpy.frombuffer 接受 buffer 输入参数，以流的形式读入转化成 ndarray 对象。
    ```
    numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
    ```
    注意：buffer是字符串的时候，Python3默认str是 Unicode类型，所以要转成bytestring在原str前加上b。默认str中不能包含非ASCII字符(<128>)

    参数| 	描述
    --|--
    buffer| 	可以是任意对象，会以流的形式读入。
    dtype| 	返回数组的数据类型，可选
    count| 	读取的数据数量，默认为-1，读取所有数据。
    offset| 	读取的起始位置，默认为0。

* numpy.fromiter
    numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。
    ```
    numpy.fromiter(iterable, dtype, count=-1)
    ```
    参数| 	描述
    --|--
    iterable| 	可迭代对象
    dtype| 	返回数组的数据类型
    count| 	读取的数据数量，默认为-1，读取所有数据

    ```
    import numpy as np 
    
    # 使用 range 函数创建列表对象  
    list=range(5)
    it=iter(list)
    
    # 使用迭代器创建 ndarray 
    x=np.fromiter(it, dtype=float)
    print(x)
    ```

### 1.4 从数值范围创建数组

* numpy.arange

    numpy 包中的使用 arange 函数创建数值范围并返回 ndarray 对象，函数格式如下：

    numpy.arange(start, stop, step, dtype)

    根据 start 与 stop 指定的范围以及 step 设定的步长，生成一个 ndarray。

    参数说明：
    参数| 	描述
    --|--
    start| 	起始值，默认为0
    stop| 	终止值（不包含）
    step| 	步长，默认为1
    dtype| 	返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。

* numpy.linspace

    numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：
    ```
    np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    ```

    参数说明：
    参数| 	描述
    --|--
    start| 	序列的起始值
    stop| 	序列的终止值，如果endpoint为true，该值包含于数列中
    num| 	要生成的等步长的样本数量，默认为50
    endpoint| 	该值为 true 时，数列中包含stop值，反之不包含，默认是True。
    retstep| 	如果为 True 时，生成的数组中会显示间距，反之不显示。
    dtype| 	ndarray 的数据类型

    以下实例用到三个参数，设置起始点为 1 ，终止点为 10，数列个数为 10。
    实例
    ```
    import numpy as np
    a = np.linspace(1,10,10)
    print(a)
    ```

* numpy.logspace

    numpy.logspace 函数用于创建一个于等比数列。格式如下：
    ```
    np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
    ```
    参数| 	描述
    --|--
    start| 	序列的起始值为：base ** start
    stop| 	序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中
    num| 	要生成的等步长的样本数量，默认为50
    endpoint| 	该值为 true 时，数列中中包含stop值，反之不包含，默认是True。
    base| 	对数 log 的底数。
    dtype| 	ndarray 的数据类型
    实例
    ```
    import numpy as np
    # 默认底数是 10
    a = np.logspace(1.0,  2.0, num =  10)  
    print (a)
    ```

## 2 dtype
数据类型

```
# 类型字段名可以用于存取实际的 age 列
import numpy as np
dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print(a['age'])


# 定义一个学生结构
import numpy as np
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print(a)

```

## 3 NumPy 切片和索引

ndarray对象的内容可以通过索引或切片来访问和修改，与 Python中list的切片操作一样。

ndarray 数组可以基于 0 - n 的下标进行索引，切片对象可以通过内置的 slice 函数，并设置 start, stop 及 step 参数进行，从原数组中切割出一个新数组。

```
import numpy as np
 
a = np.arange(10)
s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
print (a[s])
```

也可以通过冒号分隔切片参数 start:stop:step 来进行切片操作：
```
import numpy as np
 
a = np.arange(10)  
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)
```

 [2:]，表示从该索引开始以后的所有项都将被提取。如果使用了两个参数，如 [2:7]，那么则提取两个索引(不包括停止索引)之间的项。
 ```
import numpy as np
 
a = np.arange(10)
print(a[2:])
 ```

切片还可以包括省略号 …，来使选择元组的长度与数组的维度相同。 如果在行位置使用省略号，它将返回包含行中元素的 ndarray。
```
import numpy as np
 
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print (a[...,1])   # 第2列元素
print (a[1,...])   # 第2行元素
print (a[...,1:])  # 第2列及剩下的所有元素
```
结果为：
```
[2 4 5]
[3 4 5]
[[2 3]
 [4 5]
 [5 6]]
```