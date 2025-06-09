class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans=cnt=l=0
        for i,c in enumerate(nums):
            cnt+=c
            while cnt*(i-l+1)>=k:
                cnt-=nums[l]
                l+=1
            ans+=i-l+1
        return ans