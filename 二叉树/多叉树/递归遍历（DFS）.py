class Node:
    def __init__(self, val: int):
        self.val = val
        self.children = []

# 二叉树的遍历框架
def traverse_binary_tree(root):
    if root is None:
        return
    # 前序位置
    traverse_binary_tree(root.left)
    # 中序位置
    traverse_binary_tree(root.right)
    # 后序位置


# N 叉树的遍历框架
def traverse_n_ary_tree(root):
    if root is None:
        return
    # 前序位置
    for child in root.children:
        traverse_n_ary_tree(child)
    # 后序位置