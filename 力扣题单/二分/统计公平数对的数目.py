from bisect import bisect_right, bisect_left


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans=0
        for i,c in enumerate(nums):
            r=bisect_right(nums,upper-c,0,i)
            l=bisect_left(nums,lower-c,0,i)
            ans+=r-l
        return ans