class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        from collections import deque
        queue=deque()
        ans=[]
        queue.append(root)

        while queue:
            ans.append(queue[-1].val)
            sz=len(queue)
            for i in range(sz):
                cur=queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return ans
