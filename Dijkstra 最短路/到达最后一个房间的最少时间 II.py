import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n,m=len(moveTime),len(moveTime[0])
        dis=[[float('inf')]*m for _ in range(n)]
        dis[0][0]=0
        h=[(0,0,0)]
        while True:
            d,i,j=heapq.heappop(h)
            if i==n-1 and j==m-1:
                return d
            if d>dis[i][j]:
                continue
            t=(i+j)%2+1
            for di,dj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=di<n and 0<=dj<m:
                    new_dis=max(d,moveTime[di][dj])+t
                    if new_dis<dis[di][dj]:
                        dis[di][dj]=new_dis
                        heapq.heappush(h,(new_dis,di,dj))