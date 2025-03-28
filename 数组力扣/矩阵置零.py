class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        s=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    s.append((i,j))
        for a,b in s:
            for x in range(m):
                matrix[x][b]=0
            for y in range(n):
                matrix[a][y]=0

        """
        Do not return anything, modify matrix in-place instead.
        """
