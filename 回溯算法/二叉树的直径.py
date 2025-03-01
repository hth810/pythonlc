class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.maxDiameter=0
    def maxDepth(self,root):
        if root is None:
            return 0
        leftMax=self.maxDepth(root.left)
        rightMax=self.maxDepth(root.right)
        diameter=leftMax+rightMax
        self.maxDiameter=max(self.maxDiameter,diameter)

        return 1+max(leftMax,rightMax)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.maxDiameter

