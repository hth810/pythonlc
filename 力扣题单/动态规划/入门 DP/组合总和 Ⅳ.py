from functools import cache


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n=len(nums)
        @cache
        def dfs(i):
            if i==0:
                return 1
            return sum(dfs(i-x) for x in nums if x<=i)
        return dfs(target)