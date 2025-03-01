class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        s=[[0]*n for _ in range(n)]
        x,y=0,0
        k=0
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        i=1
        while True:
            s[x][y]=i
            if i==n*n:
                break
            while x+dx[k]<0 or x+dx[k]==n or y+dy[k]<0 or y+dy[k]==n or s[x+dx[k]][y+dy[k]]:
                k=(k+1)%4
            x+=dx[k]
            y+=dy[k]
            i+=1

        return s

