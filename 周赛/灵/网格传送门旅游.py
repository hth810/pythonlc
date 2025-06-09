# 传送加到队首
from collections import deque, defaultdict


class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        if matrix[-1][-1]=='#':
            return -1
        m=len(matrix)
        n=len(matrix[0])
        pos=defaultdict(list)
        for i,row in enumerate(matrix):
            for j,x in enumerate(row):
                if x.isupper():
                    pos[x].append((i,j))
        dirs=[(0,1),(0,-1),(-1,0),(1,0)]
        dis=[[float('inf')]*n for _ in range(m)]
        dis[0][0]=0
        q=deque()
        q.append((0,0))
        while q:
            x,y=q.popleft()
            d=dis[x][y]
            if x==m-1 and y==n-1:
                return d
            c=matrix[x][y]
            if c in pos:
                for px,py in pos[c]:
                    if d<dis[px][py]:
                        dis[px][py]=d
                        q.appendleft((px,py))
                del pos[c]
            for dx,dy in dirs:
                nx=x+dx
                ny=y+dy
                if 0<=nx<m and 0<=ny<n and matrix[nx][ny]!='#' and d+1<dis[nx][ny]:
                    dis[nx][ny]=d+1
                    q.append((nx,ny))
        return -1
