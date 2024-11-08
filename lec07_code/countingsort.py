# 计数排序，通常用于整数数组

def counting_sort1(k, arr):
    """计数排序，范围是 [0, k)

    Args:
        k (_type_): _description_
        arr (_type_): _description_
    """
    cache = [0 for k in range(k)]
    for key in arr:
        cache[key] += 1
    result = []
    for key, count in enumerate(cache):
        for _ in range(count):
            result.append(key)
    return result


def counting_sort2(k, arr):
    """改进版计数排序，使用嵌套列表
    不仅可以排列数值，也可以排列对象

    Args:
        k (_type_): _description_
        arr (_type_): _description_
    """
    cache = [[] for k in range(k)]       # O(k)
    for e in arr:                        # O(n)
        cache[e].append(e)
    output = []
    for key in range(k):                 # O(k)
        output.extend(cache[key])
    return output


def counting_sort3(k, arr):
    """改进版计数排序，使用前缀和，这里返回的仍然是数值而不是对象。

    Args:
        k (_type_): _description_
        arr (_type_): _description_
    """
    cache = [0 for k in range(k)]
    for key in arr:
        cache[key] += 1 
    
    for i in range(1, k):
        cache[i] = cache[i] + cache[i-1]

    counter = [0 for _ in range(len(arr))]
    for num in range(len(cache)-1, -1, -1):
        # 指针
        key = cache[num] - 1
        while key > cache[num-1] - 1:
            counter[key] = num
            key -= 1

    return counter


def counting_sort4(k, arr):
    """3 的改进，3 返回的仍然是数值而不是对象。
    
    Args:
        k (int): 数组中最大值 + 1（计数数组的大小）
        arr (list[int]): 要排序的数组
    """
    # Step 1: 统计每个数字的出现次数
    cache = [0] * k
    for num in arr:
        cache[num] += 1
    
    # Step 2: 计算前缀和
    for i in range(1, k):
        cache[i] += cache[i - 1]
    
    # Step 3: 利用前缀和填充排序后的数组
    counter = [0] * len(arr)
    for num in arr:
        # 根据 num 的前缀和位置确定它的位置
        cache[num] -= 1
        counter[cache[num]] = num
    
    return counter



if __name__ == '__main__':
    import numpy as np
    arr = np.random.randint(5, size=10, dtype=int)
    arr = counting_sort3(5, arr)
    print(arr)