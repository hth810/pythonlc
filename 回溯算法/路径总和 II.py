class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def traverse(self, root: TreeNode, targetSum: int, track: List[int]) -> None:
        if not root:
            return
        track.append(root.val)
        targetSum -= root.val
        if not root.left and not root.right and targetSum==0:
            self.res.append(track.copy())
        self.traverse(root.left, targetSum, track)
        self.traverse(root.right, targetSum, track)
        track.pop()
        targetSum += root.val
        return
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        track=[]
        self.traverse(root, targetSum,track)
        return self.res

