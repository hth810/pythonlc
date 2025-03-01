class Solution:
    def __init__(self):
        # 记录最小深度（根节点到最近的叶子节点的距离）
        self.minDepthValue = float('inf')
        # 记录当前遍历到的节点深度
        self.currentDepth = 0

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # 从根节点开始 DFS 遍历
        self.traverse(root)
        return self.minDepthValue

    def traverse(self, root: TreeNode) -> None:
        if root is None:
            return

        # 前序位置进入节点时增加当前深度
        self.currentDepth += 1

        # 如果当前节点是叶子节点，更新最小深度
        if root.left is None and root.right is None:
            self.minDepthValue = min(self.minDepthValue, self.currentDepth)

        self.traverse(root.left)
        self.traverse(root.right)

        # 后序位置离开节点时减少当前深度
        self.currentDepth -= 1