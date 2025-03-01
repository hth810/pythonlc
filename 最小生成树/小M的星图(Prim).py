import heapq

def prim(n, stars):
    # 计算距离矩阵
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = stars[i]
            x2, y2 = stars[j]
            w = (x1 - x2) ** 2 + (y1 - y2) ** 2
            distances[i][j] = w
            distances[j][i] = w

    # 初始化距离数组和最小生成树的边集合
    dist = [float('inf')] * n
    dist[0] = 0
    mst = set()
    total_cost = 0

    while len(mst) < n:
        # 找到距离最小生成树最近的顶点
        u = min((i for i in range(n) if i not in mst), key=lambda x: dist[x])
        mst.add(u)

        # 更新距离数组
        for v in range(n):
            if v not in mst and distances[u][v] < dist[v]:
                dist[v] = distances[u][v]

        # 计算最小生成树的总权重
        total_cost += dist[u]

    return total_cost

n = int(input())
stars = []
for _ in range(n):
    x, y = map(int, input().split())
    stars.append((x, y))

print(prim(n, stars))