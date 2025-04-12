# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans=None
        mx=-1
        def dfs(node,depth):
            nonlocal ans,mx
            if node is None:
                mx=max(mx,depth)
                return depth
            l=dfs(node.left,depth+1)
            r=dfs(node.right,depth+1)
            if l==r==mx:
                ans=node
            return max(l,r)
        dfs(root,0)
        return ans