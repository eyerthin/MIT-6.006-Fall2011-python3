# 二叉搜索树

class Node:
    """二叉搜索树的节点
    """

    def __init__(self, value):
        self.value = value
        self.left: None | Node = None
        self.right: None | Node = None
        self.parent: None | Node = None


def bst_insert(root: Node, value):
    """对二叉搜索树进行插值
    """
    # 重复值违反二叉树定义
    if root.value == value:
        return
    if value < root.value:
        if root.left:
            bst_insert(root.left, value)
        else:
            root.left = Node(value)
            root.left.parent = root
    elif value > root.value:
        if root.right:
            bst_insert(root.right, value)
        else:
            root.right = Node(value)
            root.right.parent = root


def bst_insert_list(arr: list):
    """将数组列表转化为二叉搜索树

    Args:
        arr (list): _description_
    """
    node = Node(arr[0])
    for i in range(1, len(arr)):
        bst_insert(node, arr[i])
    return node

def bst_search(root: Node, value) -> bool:
    """从二叉搜索树中查找某个值知否存在

    Args:
        root (Node): _description_
        value (_type_): _description_
    """
    if root.value == value:
        return True
    if root.value > value:
        if root.left is None:
            return False
        else:
            bst_search(root.left, value)
            return True
    if root.right is None:
        return False
    else:
        bst_search(root.right, value)
        return True

def bst_delete(node: Node, value):
    """从二叉搜索树中删除某个值
    1. 没有子节点（叶结点）：直接进行删除
    2. 节点只有一个子节点：删除该节点，使其父节点连接子节点
    3. 节点有两个子节点：找到该结点的右子树的最小节点或者左子树的最大节点
    Args:
        node (Node): _description_
        value (_type_): _description_
    """
    if value < node.value and node.left is not None:
        bst_delete(node.left, value)
    elif value > node.value and node.right is not None:
        bst_delete(node.right, value)
    elif value == node.value:
        # 没有子节点
        if node.left is None \
                and node.right is None \
                and node.parent is not None:
            # 取消连接
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        # 一个子节点
        elif node.left is None and node.parent:
            if node == node.parent.left:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        elif node.right is None and node.parent:
            if node == node.parent.left:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        # 两个子节点，取左子树最大节点
        elif node.parent:
            tmp = node.left
            while tmp.right is not None:
                tmp = tmp.right
            node.value = tmp.value
            bst_delete(tmp, tmp.value)
            
def print_inorder(root: Node):
    """打印二叉搜索树的元素

    Args:
        root (Node): _description_
    """
    if root.left is not None:
        print_inorder(root.left)
    print(f'value: {root.value:.2f}')
    if root.right is not None:
        print_inorder(root.right)

def bst_invert(node: Node):
    """翻转二叉搜索树

    Args:
        node (Node): _description_
    """
    if node == None:
        return None
    node.left = bst_invert(node.right)
    node.right = bst_invert(node.left)
    return node

def printTree(root: Node, level=0, prefix="Root: "):
    if root is not None:
        # 打印当前节点
        print(" " * (level * 4) + prefix + str(root.value))
        # 递归打印左子树
        if root.left:
            printTree(root.left, level + 1, "L--- ")
        else:
            print(" " * ((level + 1) * 4) + "L--- None")
        # 递归打印右子树
        if root.right:
            printTree(root.right, level + 1, "R--- ")
        else:
            print(" " * ((level + 1) * 4) + "R--- None")


