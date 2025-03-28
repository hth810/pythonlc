class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        ans=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s=set()
                x,y=i-1,j-1
                while x>=0 and y>=0:
                    s.add(grid[x][y])
                    x-=1
                    y-=1
                top=len(s)
                s.clear()
                x,y=i+1,j+1
                while x<m and y<n:
                    s.add(grid[x][y])
                    x+=1
                    y+=1
                bot=len(s)
                ans[i][j]=abs(top-bot)

        return ans