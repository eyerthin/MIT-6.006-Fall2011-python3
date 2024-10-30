## Python成本模型

Python 作为高级语言，具备很多强大的语法，分析 Python 程序的运行时间需要了解各种 Python 语法的成本。
比如：在 Python 中，可以使用：
```python
L = L1 + L2
```
其中，L、L1、L2 都是列表；给定的语句将 L 计算为两个输入列表 L1 和 L2 的拼接。该语句的运行时间取决于列表 L1 和 L2 的长度（运行时间或多或少与这两个列表的长度总和成正比）。

## 运行时间实验及讨论
测量不同大小输入的运行时间，然后使用最小二乘拟合模型来估计函数的运行时间。(哪个项是高阶项是通过实验确定的)
最小二乘拟合旨在使用 scipy.optimize.leastsq 最小化相对误差的平方和
（该程序的早期版本不仅适用于高阶项，还适用于低阶项的系数。但是插值程序在区分 $ n $ 和 $ n \log n $ 时效果比较差，最后认为只查看高阶项并研究相对误差是最简单的。）
这里的代码没有转化为 python3 版本，python3在部分运算上性能会更优秀，但不会有数量级上的变化。
这里推荐使用conda创建python2环境
```python
conda create env -n python27 python=2.7
conda activate python27
conda install scipy
python ./timing.py > ./simple_output.txt
```

## Python整数运算成本
x、y 和 z 是 n 位数，w 是 2n 位数，s 是 n 位字符串
| **Convert string to integer** | int(s)     | 84 * (n/1000)^2 microseconds        | n <= 8000   | 6% rms error  |
| ----------------------------- | ---------- | ----------------------------------- | ----------- | ------------- |
| **Convert integer to string** | str(x)     | 75 * (n/1000)^2 microseconds        | n <= 8000   | 3% rms error  |
| **Convert integer to hex**    | “%x”%x     | 2.7 * (n/1000) microseconds         | n <= 64000  | 19% rms error |
| **Addition (or Subtraction)** | x+y        | 0.75 * (n/1000) microseconds        | n <= 512000 | 8% rms error  |
| **Multiplication**            | x\*y       | 13.73 * (n/1000)^1.585 microseconds | n <= 64000  | 10% rms error |
| **Division (or Remainder)**   | w/x        | 47 * (n/1000)^2 microseconds        | n <= 32000  | 6% rms error  |
| **Modular Exponentiation**    | pow(x,y,z) | 60000 * (n/1000)^3 microseconds     | n <= 4000   | 8% rms error  |
| **n-th power of two**         | 2**n       | 0.06 microseconds                   | n <= 512000 | 10% rms error |  

乘法使用Karatsuba算法，乘法的运行时间是 $ \Theta(n \log 3)$ ，除法为 $ n^2 $
## Python字符串运算成本
s 和 t 是长度为 n 的字符串，u 是长度为 $ n/2 $ 的字符串
| **Extract a byte from a string** | s[i]             | 0.13 microseconds           | n <= 512000 | 29% rms error |
| -------------------------------- | ---------------- | --------------------------- | ----------- | ------------- |
| **Concatenate**                  | s+t              | 1 * (n/1000) microseconds   | n <= 256000 | 19% rms error |
| **Extract string of length n/2** | s[0:n2]          | 0.3 * (n/1000) microseconds | n <= 256000 | 28% rms error |
| **Translate a string**           | s.translate(s,T) | 3.2 * (n/1000) microseconds | n <= 256000 | 11% rms error |
## Python列表运算成本
L 和 M 是长度为 n 的列表，P 的长度为 $n/2$
| **Create an empty list** | list()      | 0.40 microseconds             | (n=1)       | .5% rms error  |
| ------------------------ | ----------- | ----------------------------- | ----------- | -------------- |
| **Access**               | L[i]        | 0.10 microseconds             | n <= 640000 | 3% rms error   |
| **Append**               | L.append(0) | 0.24 microseconds             | n <= 640000 | 3% rms error   |
| **Pop**                  | L.pop()     | 0.25 microseconds             | n <= 64000  | 0.5% rms error |
| **Concatenate**          | L+M         | 22 * (n/1000) microseconds    | n <= 64000  | 3% rms error   |
| **Slice extraction**     | L[0:n2]     | 5.4 * (n/1000) microseconds   | n <= 64000  | 4% rms error   |
| **Copy**                 | L[:]        | 11.5 * (n/1000) microseconds  | n <= 64000  | 10% rms error  |
| **Slice assignment**     | L[0:n2] = P | 11 * (n/1000) microseconds    | n <= 64000  | 4% rms error   |
| **Delete first**         | del L[0]    | 1.7 * (n/1000) microseconds   | n <= 64000  | 4% rms error   |
| **Reverse**              | L.reverse() | 1.3 * (n/1000) microseconds   | n <= 64000  | 10% rms error  |
| **Sort**                 | L.sort()    | 0.0039 * n lg(n) microseconds | n <= 64000  | 12% rms error  |  

Python中的列表是通过可变数组实现的，每次超出范围，都会花费额外的时间把之前所有内容都复制一遍，并在末尾添加额外的空间（大约占原列表的$1/8$）

## Python字典运算成本
D 是一个有 n 对键值对的字典
| **Create an empty dictionary** | dict()    | 0.36 microseconds             | (n=1)      | 0% rms error  |
| ------------------------------ | --------- | ----------------------------- | ---------- | ------------- |
| **Access**                     | D[i]      | 0.12 microseconds             | n <= 64000 | 3% rms error  |
| **Copy**                       | D.copy()  | 57 * (n/1000) microseconds    | n <= 64000 | 27% rms error |
| **List items**                 | D.items() | 0.0096 * n lg(n) microseconds | n <= 64000 | 14% rms error |  

复制项和列表项的右高阶项应该是什么？似乎应该是线性的，但两者的数据看起来都有点超线性。在这里，我们将复制建模为线性，将列表项建模为 $n lg(n)$，但这些公式还需要进一步研究和探索。