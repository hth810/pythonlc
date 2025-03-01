# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        queue=deque()
        queue.append(root)
        ans=[]
        while queue:
            nxt=[]
            vals=[]
            for i in queue:
                vals.append(i.val)
                if i.left:
                    nxt.append(i.left)
                if i.right:
                    nxt.append(i.right)
            queue=nxt
            ans.append(vals)
        return ans[-1][0]
