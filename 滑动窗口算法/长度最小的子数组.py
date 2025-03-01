class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        l,r=0,0
        length=len(nums)+1
        while r<len(nums):
            c=nums[r]
            r+=1
            sum+=c
            while sum>=target:
                if r-l<length:
                    length=r-l
                sum-=nums[l]
                l+=1
        return 0 if length==len(nums)+1 else length