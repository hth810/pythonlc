class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traverse(self,root):
        if not root:
            return
        temp=root.left
        root.left=root.right
        root.right=temp
        self.traverse(root.left)
        self.traverse(root.right)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root