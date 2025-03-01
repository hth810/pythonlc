class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def dfs(i):
            if i*2>=n:
                return prices[i-1]
            return min(dfs(j) for j in range(i+1,i*2+2))+prices[i-1]
        return dfs(1)