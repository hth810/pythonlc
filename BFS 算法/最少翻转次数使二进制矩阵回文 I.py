class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        row,col=0,0
        for i in range(m):
            for j in range(n//2):
                if grid[i][j]!=grid[i][n-1-j]:
                    row+=1
        for i in range(n):
            for j in range(m//2):
                if grid[j][i]!=grid[m-1-j][i]:
                    col+=1

        return min(row,col)