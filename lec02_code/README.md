这里是lec02的案例
作用为通过向量内积计算文本相似度
将原内容重构为了 python3 版本
主要区别在 dict.items 不同
```python
# python2
>>> dict1 = dict(zip('ABCDE', range(5)))
>>> dict1.items()
[('A', 0), ('C', 2), ('B', 1), ('E', 4), ('D', 3)]

# python3
>>> dict1 = dict(zip('ABCDE', range(5)))
>>> dict1.items()
dict_items([('A', 0), ('B', 1), ('C', 2), ('D', 3), ('E', 4)])
```

*推荐使用diff查看各个版本的不同*
*可以尝试使用其他性能分析工具，比如line_profiler*