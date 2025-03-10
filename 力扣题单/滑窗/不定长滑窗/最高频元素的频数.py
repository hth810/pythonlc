class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        temp=0
        ans=0
        l=0
        for r,c in enumerate(nums):
            temp+=c
            while temp+k<c*(r-l+1) and l<r:
                temp-=nums[l]
                l+=1
            ans=max(ans,r-l+1)
        return ans