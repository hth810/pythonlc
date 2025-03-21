from functools import cache


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        @cache
        def dfs(i):
            if i>=n:
                return 0
            return min(dfs(i+1)+cost[i],dfs(i+2)+cost[i])

        ans=min(dfs(0),dfs(1))

        return ans