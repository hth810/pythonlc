MOD=10**9+7
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        u = 1 << max(map(max, grid)).bit_length()
        if k >= u:
            return 0
        f=[[[0]*u for _ in range(n+1)]for _ in range(m+1)]
        f[0][1][0]=1
        for i,row in enumerate(grid):
            for j,x in enumerate(row):
                for a in range(u):
                    f[i+1][j+1][a]+=(f[i+1][j][a^x]+f[i][j+1][x^a])%MOD
        return f[m][n][k]