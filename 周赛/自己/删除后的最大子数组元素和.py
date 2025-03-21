class Solution:
    def maxSum(self, nums: List[int]) -> int:
        a=set()
        for i,c in enumerate(nums):
            if c>=0:
                a.add(c)
        return sum(a) if max(nums)>=0 else max(nums)