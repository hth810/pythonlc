from functools import cache
MOD=10**9+7

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        @cache
        def dfs(i,j):
            if i==0 and j==0:
                return (grid[i][j],grid[i][j])
            res=grid[i][j]
            mx,mn=float('-inf'),float('inf')
            if i>0:
                a,b=dfs(i-1,j)
                mx,mn=max(res*a,res*b,mx),min(res*a,res*b,mn)
            if j>0:
                a,b=dfs(i,j-1)
                mx,mn=max(res*a,res*b,mx),min(res*a,res*b,mn)
            return (mx,mn)
        ans=dfs(m-1,n-1)[0]
        return ans%MOD if ans>=0 else -1