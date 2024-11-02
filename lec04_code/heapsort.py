# 堆排序，首先你得有个堆

def max_heapify(arr, i, N):
    """ 
    将列表进行最大堆堆化，使每个父节点的值都大于子节点。
    arr: 数组
    i: 父节点
    N: 节点总数

    时间复杂度为: O(logN)
    每个节点的堆化花费时间为 log(i)
    """
    left = i << 1
    right = left + 1
    largest = i
    # 左子节点，右子节点。

    # 1. 节点不超出范围
    # 2. 父节点小于子节点的话以子节点为父节点继续分析
    if left < N and arr[largest] < arr[left]:
        largest = left
    if right < N and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, N)


def build_max_heap(arr):
    """ 
    根据数组建立大顶堆
    """
    for i in range(len(arr) //2, -1, -1):
        max_heapify(arr, i, len(arr))
    return arr

def heapsort(arr):
    """
    堆排序
    """
    build_max_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)
    return arr

if __name__ == '__main__':
    import numpy as np
    arr = np.random.randint(100, size=10)
    print(heapsort(arr))