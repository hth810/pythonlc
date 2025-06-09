from collections import deque
MOD=10**9+7

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        def lca(u, v):
            if d[u] < d[v]:
                u, v = v, u
            for k in range(19, -1, -1):
                if d[u] - (1 << k) >= d[v]:
                    u = up[k][u]
            if u == v:
                return u
            for k in range(19, -1, -1):
                if up[k][u] != -1 and up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return pa[u]
        n=len(edges)+1
        tree=[[] for _ in range(n+1)]
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
        d=[0]*(n+1)
        d[1]=0
        pa=[-1]*(n+1)
        up=[[-1]*(n+1) for _ in range(20)]
        q=deque()
        q.append(1)
        pa[1]=-1
        while q:
            i=q.popleft()
            for j in tree[i]:
                if pa[j]==-1 and j!=1:
                    pa[j]=i
                    d[j]=d[i]+1
                    q.append(j)
        for u in range(1, n + 1):
            up[0][u] = pa[u]
        for k in range(1, 20):
            for u in range(1, n + 1):
                if up[k - 1][u] != -1:
                    up[k][u] = up[k - 1][up[k - 1][u]]
        res=[]
        for u,v in queries:
            if u==v:
                res.append(0)
                continue
            a=lca(u,v)
            m=d[u]+d[v]-2*d[a]
            if m==0:
                res.append(0)
            else:
                res.append(pow(2,m-1,MOD))
        return res

