from collections import deque


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n=len(obstacles)
        dis=[[n]*3 for _ in range(n)]
        dis[0][1]=0
        q=deque()
        q.append((0,1))
        while q:
            i,j=q.popleft()
            d=dis[i][j]
            if i==n-1:
                return d
            if obstacles[i+1]!=j+1 and d<dis[i+1][j]:
                dis[i+1][j]=d
                q.appendleft((i+1,j))
            for k in (j+1)%3,(j+2)%3:
                if obstacles[i]!=k+1 and d+1<dis[i+1][j]:
                    dis[i][k]=d+1
                    q.append((i,k))
