class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = False
    def traverse(self, root: TreeNode, targetSum: int) -> None:
        if not root:
            return
        targetSum -= root.val
        if not root.left and not root.right:
            if targetSum == 0:
                self.res = True
            return
        self.traverse(root.left, targetSum)
        self.traverse(root.right, targetSum)
        targetSum += root.val
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.traverse(root, targetSum)
        return self.res
