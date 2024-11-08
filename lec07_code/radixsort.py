# 基数排序，适用于数据量 n 较大，但是数据范围 m 较小的情况。

def get_digit(num: int, exp: int) -> int:
    """返回 num 的第 k 位 的数值， exp=10**(k-1)
    这里使用可以避免重复进行昂贵的次方运算

    Args:
        num (int): _description_
        exp (int): _description_

    Returns:
        int: _description_
    """
    return (num // exp) % 10

def countingsort_digit(nums: list[int], exp: int):
    """计数排序，对 nums 的第 k 位进行排序

    Args:
        nums (list[int]): _description_
        exp (int): _description_
    """
    # 这里以十进制为例，每一位都可能是 0-9 
    counter = [0] * 10
    n = len(nums)
    # 计算第 k 位出现的次数
    for i in range(n):
        d = get_digit(nums[i], exp)
        counter[d] += 1
    # 求前缀和
    for i in range(1, 10):
        counter[i] = counter[i] + counter[i - 1]
    
    result = [0] * n
    for i in range(n-1, -1, -1):
        d = get_digit(nums[i], exp)
        # 获取数值 d 的索引
        j = counter[d] - 1
        # 将当前位置的元素传入 result 对应的索引
        result[j] = nums[i]
        counter[d] -= 1
    for i in range(n):
        nums[i] = result[i]


def radixsort(nums: list[int]):
    """基数排序

    Args:
        nums (list[int]): _description_
    """
    # 使用最大元素获取最大位数
    m = max(nums)
    exp = 1
    while exp <= m:
        # 对数字第 k 位执行计数排序
        countingsort_digit(nums, exp)
        exp *= 10


if __name__ == '__main__':
    import numpy as np
    arr = np.random.randint(10**7, 10**8-1, size=20)
    radixsort(arr)
    print(arr)