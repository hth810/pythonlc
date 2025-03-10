from bisect import bisect_right, bisect_left


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans=0
        for j,v in enumerate(nums):
            r=bisect_right(nums,upper-v,0,j)
            l=bisect_left(nums,lower-v,0,j)
            ans+=r-l
        return ans