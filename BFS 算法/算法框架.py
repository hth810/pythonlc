from collections import deque

class Node:
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []

def BFS(start: Node, target: Node) -> int:
    # 核心数据结构
    q = deque()
    # 避免走回头路
    visited = set()
    # 将起点加入队列
    q.append(start)
    visited.add(start)

    # 记录扩散的步数
    step = 0

    while q:
        step += 1
        size = len(q)
        # 将当前队列中的所有节点向四周扩散
        for i in range(size):
            cur = q.popleft()
            # 划重点：这里判断是否到达终点
            if cur == target:
                return step
            # 将cur相邻节点加入队列
            for x in cur.neighbors:
                if x not in visited:
                    q.append(x)
                    visited.add(x)
    # 如果走到这里，说明在图中没有找到目标节点
    return -1