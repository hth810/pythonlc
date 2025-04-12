class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        f=[[float('inf')]*n for _ in range(n)]
        for i in range(n):
            f[0][i]=grid[0][i]
        for i in range(1,n):
            for j in range(n):
                for k in range(n):
                    if k==j:
                        continue
                    f[i][j]=min(f[i][j],f[i-1][k]+grid[i][j])
        return min(f[-1])