class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        f=[[0]*(n+1) for _ in range(m+1)]
        f[0]=list(range(n+1))
        for i,x in enumerate(word1):
            f[i+1][0]=i+1
            for j,y in enumerate(word2):
                if x==y:
                    f[i+1][j+1]=f[i][j]
                else:
                    f[i+1][j+1]=min(f[i][j+1],f[i+1][j],f[i][j])+1
        return f[m][n]