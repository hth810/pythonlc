class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import cache
        n=len(prices)
        @cache
        def dfs(i,hold):
            if i<0:
                return -float('inf') if hold else 0
            if hold:
                return max(dfs(i-1,True),dfs(i-2,False)-prices[i])
            return max(dfs(i-1,False),dfs(i-1,True)+prices[i])
        return dfs(n-1,False)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n=len(prices)
#         f=[[0]*2 for _ in range(n+1)]
#         f[0][1]=-float('inf')
#         for i,p in enumerate(prices):
#             f[i+1][0]=max(f[i][0],f[i][1]+p)
#             f[i+1][1]=max(f[i][1],f[i][0]-p)
#         return f[n][0]