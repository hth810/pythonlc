class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        size=m*n
        x=y=0
        k=0
        step=1
        ans=[]
        vis=[]
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        while True:
            vis.append((x,y))
            ans.append(matrix[x][y])
            if step==size:
                break
            while x+dx[k]<0 or x+dx[k]==m or y+dy[k]<0 or y+dy[k]==n or (x+dx[k],y+dy[k]) in vis:
                k=(k+1)%4
            x+=dx[k]
            y+=dy[k]
            step+=1
        return ans

