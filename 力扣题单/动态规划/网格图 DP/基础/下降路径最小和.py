class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        f=[[float('inf')]*(n+2) for _ in range(n+1)]
        for i,row in enumerate(matrix):
            for j,x in enumerate(row):
                if i==0:
                    f[1][j+1]=x
                else:
                    f[i+1][j+1]=min(f[i][j],f[i][j+1],f[i][j+2])+matrix[i][j]
        return min(f[n][i]for i in range(1,n+1))

