from functools import cache


class Solution:
    def minCost(self, nums: List[int]) -> int:
        n=len(nums)
        @cache
        def dfs(i,pre):
            if i==n:
                return pre
            if i==n-1:
                return max(pre,nums[-1])
            temp=sorted([pre,nums[i],nums[i+1]])
            return min(temp[2]+dfs(i+2,temp[0]),temp[1]+dfs(i+2,temp[2]))
        if n<3:
            return max(nums)
        temp=sorted(nums[:3])
        return min(temp[2]+dfs(3,temp[1]),temp[1]+dfs(3,temp[2]))