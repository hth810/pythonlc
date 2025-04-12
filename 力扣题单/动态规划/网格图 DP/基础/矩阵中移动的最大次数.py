class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        ans=0
        def dfs(i,j):
            nonlocal ans
            ans=max(ans,j)
            if j==n-1:
                return
            for k in i-1,i,i+1:
                if 0<=k<m and grid[k][j+1]>grid[i][j]:
                    dfs(k,j+1)
            grid[i][j]=0
        for i in range(m):
            dfs(i,0)
        return ans