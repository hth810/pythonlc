from bisect import bisect_right
from functools import cache

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        n=len(rewardValues)
        @cache
        def dfs(c):
            i=bisect_right(rewardValues,c)
            if i>=n:
                return 0
            res=0
            for a in rewardValues[i:]:
                res=max(res,a+dfs(c+a))
            return res
        return dfs(0)