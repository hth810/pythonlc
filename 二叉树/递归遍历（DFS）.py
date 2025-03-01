# 基本的二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 二叉树的遍历框架
def traverse(root: TreeNode):
    if root is None:
        return
    traverse(root.left)
    traverse(root.right)

# traverse 函数的遍历顺序就是一直往左子节点走，直到遇到空指针不能再走了，才尝试往右子节点走一步；然后再一直尝试往左子节点走，
# 如此循环；如果左右子树都走完了，则返回上一层父节点。其实看代码也能看出来，先递归调用的 root.left，然后才递归调用的 root.right 嘛