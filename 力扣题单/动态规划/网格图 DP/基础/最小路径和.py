class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        f=[[float('inf')]*(n+1) for _ in range(m+1)]
        for i,row in enumerate(grid):
            for j,v in enumerate(row):
                if i==j==0:
                    f[1][1]=v
                else:
                    f[i+1][j+1]=min(f[i][j+1],f[i+1][j])+v
        return f[m][n]