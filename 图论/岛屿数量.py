class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or i>m-1 or j<0 or j>n-1 or grid[i][j]!='1':
                return
            grid[i][j]='2'
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        ans=0
        for i,row in enumerate(grid):
            for j,c in enumerate(row):
                if c=='1':
                    dfs(i,j)
                    ans+=1
        return ans