class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target+=sum(nums)
        if target<0 or target%2:
            return 0
        target//=2
        n=len(nums)
        @cache
        def dfs(i,c):
            if i<0:
                return 1 if c==0 else 0
            if c<nums[i]:
                return dfs(i-1,c)
            return dfs(i-1,c)+dfs(i-1,c-nums[i])
        return dfs(n-1,target)
