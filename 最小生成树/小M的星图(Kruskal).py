class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    cost = 0
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            cost += w
    return cost

n = int(input())
stars = []
for _ in range(n):
    x, y = map(int, input().split())
    stars.append((x, y))

edges = []
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        w = (x1 - x2) ** 2 + (y1 - y2) ** 2
        edges.append((i, j, w))

print(kruskal(n, edges))