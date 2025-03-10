class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        ans=0
        for r,c in enumerate(nums):
            while c-nums[l]>k*2:
                l+=1
            ans=max(ans,r-l+1)
        return ans