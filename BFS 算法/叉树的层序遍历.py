# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        queue=deque()
        ans=[]
        queue.append(root)
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
        return ans