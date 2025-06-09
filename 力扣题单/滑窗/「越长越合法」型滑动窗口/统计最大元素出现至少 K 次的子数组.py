class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx=max(nums)
        cnt=0
        ans=0
        l=0
        for i,c in enumerate(nums):
            if c==mx:
                cnt+=1
            while cnt==k:
                d=nums[l]
                if d==mx:
                    cnt-=1
                l+=1
            ans+=l
        return ans