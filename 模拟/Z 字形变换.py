class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        matrix=[[""]*1000 for _ in range(numRows)]
        x=0
        y=0
        i=0
        k=0
        dx=[1,-1]
        dy=[0,1]
        matrix[x][y]=s[i]
        ans=""
        while i<len(s)-1:
            i+=1
            if x+dx[k]==numRows or x+dx[k]<0:
                k=(k+1)%2
            x+=dx[k]
            y+=dy[k]
            matrix[x][y]=s[i]
        for a in range(numRows):
            for b in range(len(s)):
                if matrix[a][b]!="":
                    ans+=matrix[a][b]

        return ans

