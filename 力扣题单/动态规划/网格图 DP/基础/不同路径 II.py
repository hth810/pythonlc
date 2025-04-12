class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        f=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if i==j==0 and obstacleGrid[i][j]!=1:
                    f[1][1]=1
                elif obstacleGrid[i][j]==1:
                    f[i+1][j+1]=0
                else:
                    f[i+1][j+1]=f[i+1][j]+f[i][j+1]
        return f[m][n]