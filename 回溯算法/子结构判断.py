class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubStructure(self, A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:
        if A==None or B==None:
            return False
        return self.compare(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)
    def compare(self,A,B):
        if B==None:
            return True
        if A==None:
            return False
        return A.val==B.val and self.compare(A.left,B.left) and self.compare(A.right,B.right)
