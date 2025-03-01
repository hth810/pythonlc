from functools import cache


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        @cache
        def dfs(m,n):
            if obstacleGrid[m][n]==1:
                return 0
            if m==0 and n==0:
                return 1
            if m<0:
                return 0
            if n<0:
                return 0
            return dfs(m-1,n)+dfs(m,n-1)
        return dfs(m-1,n-1)