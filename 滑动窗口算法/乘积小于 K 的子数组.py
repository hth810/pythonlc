class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        prod=1
        ans=0
        l=0
        for r,c in enumerate(nums):
            prod*=c
            while prod>=k:
                prod=prod//nums[l]
                l+=1
            else:
                ans+=r-l+1

        return ans