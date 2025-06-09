class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=[]
        m,n=len(grid),len(grid[0])
        fresh=0
        for i,row in enumerate(grid):
            for j,c in enumerate(row):
                if c=='2':
                    q.append((i,j))
                elif c=='1':
                    fresh+=1
        ans=0
        while q and fresh:
            ans+=1
            tmp=q
            q=[]
            for x,y in tmp:
                for dx,dy in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if 0<=dx<m and 0<=dy<n and grid[dx][dy]==1:
                        fresh-=1
                        grid[dx][dy]=2
                        q.append((dx,dy))
        return ans