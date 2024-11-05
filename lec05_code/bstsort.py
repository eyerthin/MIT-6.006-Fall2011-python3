# 二叉搜索树排序
# 中序遍历得到从小到大的有序序列

from bst import *
import numpy as np

def inorderTraversal(node: Node):
    result = []
    if node:
        result = inorderTraversal(node.left)
        result.append(node.value)
        result = result + inorderTraversal(node.right)
    return result

def main():
    arr = np.random.randint(100, size=10)
    arr_node = bst_insert_list(arr)
    sort_arr = inorderTraversal(arr_node)
    print(sort_arr)
    printTree(arr_node)

if __name__ == "__main__":
    main()

