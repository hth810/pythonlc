class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        f=[[]for _ in range(n+1)]
        for i,j,k in roads:
            f[i].append((j,k))
            f[j].append((i,k))
        ans=float('inf')
        vis=[0]*(n+1)
        def dfs(i):
            nonlocal ans

            vis[i]=1
            for a,b in f[i]:
                ans = min(ans, b)
                if vis[a]==0:
                    dfs(a)
        dfs(1)
        return ans

