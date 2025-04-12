from functools import cache


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        @cache
        def dfs(i,j):
            if i==m-1:
                return grid[i][j]
            cnt=float('inf')
            for c,k in enumerate(moveCost[grid[i][j]]):
                cnt=min(cnt,dfs(i+1,c))+k
            return cnt+grid[i][j]
        return min(dfs(0,k) for k in range(n))