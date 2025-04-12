from functools import cache


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        @cache
        def dfs(i,j,k):
            if i<0 or j<0:
                return float('-inf')
            x=coins[i][j]
            if i==0 and j==0:
                return max(x,0) if k else x
            res=max(dfs(i-1,j,k),dfs(i,j-1,k))+x
            if x<0 and k:
                res=max(res,dfs(i-1,j,k-1),dfs(i,j-1,k-1))
            return res
        return dfs(len(coins)-1,len(coins[0])-1,2)