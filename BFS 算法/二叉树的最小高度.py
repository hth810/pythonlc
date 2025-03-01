class Solution:
    def minDepth(self, root):
        from collections import deque
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        # root 本身就是一层，depth 初始化为 1
        depth = 1

        while queue:
            sz = len(queue)
            # 将当前队列中的所有节点向四周扩散
            for i in range(sz):
                cur = queue.popleft()
                # 判断是否到达终点
                if not cur.left and not cur.right:
                    return depth
                # 将 cur 的相邻节点加入队列
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            # 这里增加步数
            depth += 1
        return depth