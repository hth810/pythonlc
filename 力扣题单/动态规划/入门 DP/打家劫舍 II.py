from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        a=nums[:-1]
        b=nums[1:]
        @cache
        def dfs(i):
            if i<0:
                return 0
            return max(dfs(i-1),dfs(i-2)+a[i])
        @cache
        def dfs1(i):
            if i<0:
                return 0
            return max(dfs1(i-1),dfs1(i-2)+b[i])
        return max(dfs(n-2),dfs1(n-2))
