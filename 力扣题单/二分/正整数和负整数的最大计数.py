from bisect import bisect_left, bisect_right


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=len(nums)
        a=bisect_left(nums,0)
        b=bisect_right(nums,0)
        res=max(a,n-b)
        return res