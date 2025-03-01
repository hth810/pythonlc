class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        @cache
        def dfs(row,col):
            if col<0 or col>=n:
                return float('inf')
            if row==0:
                return matrix[0][col]
            return min(dfs(row-1,col-1),dfs(row-1,col),dfs(row-1,col+1))+matrix[row][col]
        return min(dfs(n-1,i) for i in range(n))
