class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def judge(self,p: Optional[TreeNode],q: Optional[TreeNode]):
        if p is None or q is None:
            return p is q
        return p.val==q.val and self.judge(p.left,q.right) and self.judge(p.right,q.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.judge(root.left,root.right)
