### 二叉搜索树

时间复杂度主要和数的结构有关系，平衡树效率最好，退化成链表效率最差。  
插入操作：
    * 平衡树：每比较一次深度（二叉树的边长）减一，树的高度为 $O(logn)$，时间复杂度为 $O(logn)$。
    * 链表：每个节点只有一个子节点，时间复杂度为 $O(n)$。
查找操作：
    * 平衡树：$O(logn)$
    * 链表：$O(n)$
删除操作:
    * 平衡树：$O(logn)$
    * 链表：$O(n)$
中序遍历：
    * 时间复杂度和数的结构没有关系，只和节点数量有关 $O(n)$。
翻转操作：
    * 遍历整个树，交换左右子树，$O(n)。

空间复杂度
插入、查找、删除：
    * 平衡树：递归实现，递归深度为 $O(logn)$，空间复杂度为 $O(logn)$。
    * 链表：$O(n)$
中序遍历，翻转：
    * 平衡树：递归，调用的深度和树的高度有关系，$O(logn)$
    * 链表：$O(n)$