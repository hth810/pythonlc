from functools import cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def dfs(i,hold):
            if i<0:
                return float('-inf') if hold else 0
            if hold:
                return max(dfs(i-1,1),dfs(i-1,0)-prices[i])
            return max(dfs(i-1,0),dfs(i-1,1)+prices[i])
        return dfs(n-1,0)