from functools import cache


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        a=[0]*(max(nums)+1)
        for i in nums:
            a[i]+=i
        @cache
        def dfs(i):
            if i<0:
                return 0
            return max(dfs(i-1),dfs(i-2)+a[i])

        return dfs(len(a)-1)