from bst import *

if __name__ == '__main__':
    import numpy as np
    arr = np.random.randint(100, size=10)
    arr_node = bst_insert_list(arr)
    printTree(arr_node)
    # print_inorder(arr_node)