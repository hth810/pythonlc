from functools import cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        s=sum(nums)
        if (s+target)%2:
            return 0
        tgt=(s+target)//2
        @cache
        def dfs(i,j):
            if i<0 :
                return 1 if j==0 else 0
            if j<nums[i]:
                dfs(i-1,j)
            return dfs(i-1,j-nums[i])+dfs(i-1,j)
        return dfs(n-1,tgt)