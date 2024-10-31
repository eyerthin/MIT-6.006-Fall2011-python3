import numpy as np

def merge(left, right):
    """ 
    将两个排序好的序列合并
    复杂度: O(m+n)
    m = len(left), n = len(right)
    """
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])
    return result

def mergesort(L):
    """ 
    合并排序
    复杂度： O(n * log(n))
    """
    n = len(L)
    if n == 1:
        return L
    left = mergesort(L[:n//2])
    right = mergesort(L[n//2:])
    return merge(left, right)

if __name__ == '__main__':
    L = np.random.randint(100, size=10)
    print(mergesort(L))