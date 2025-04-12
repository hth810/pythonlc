from functools import cache


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        @cache
        def dfs(i,j):
            if i==n-1:
                return triangle[i][j]
            return min(dfs(i+1,j),dfs(i+1,j+1))+triangle[i][j]
        return dfs(0,0)