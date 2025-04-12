from bisect import bisect_left


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        n=len(nums)
        idx=bisect_left(nums,1)
        if idx==n:
            return 1
        if nums[idx]!=1:
            return 1
        for i in range(idx,n):
            if nums[i]!=i-idx+1:
                return i-idx+1
        return nums[-1]+1
