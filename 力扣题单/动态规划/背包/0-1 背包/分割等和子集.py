from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i,j):
            if i<0:
                return j==0
            return j>=nums[i] and dfs(i-1,j-nums[i]) or dfs(i-1,j)
        n=len(nums)
        s=sum(nums)
        if s%2:
            return False
        s//=2
        return dfs(n-1,s)