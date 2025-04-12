# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return False
            if not dfs(node.left):
                node.left=None
            if not dfs(node.right):
                node.right=None
            return node.val==1 or node.left or node.right
        return root if dfs(root) else None

