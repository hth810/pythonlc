# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        queue=deque()
        ans=[]
        queue.append(root)
        j=0
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
            if j%2==1:
                vals=vals[::-1]
            ans.append(vals)
            j+=1
        return ans