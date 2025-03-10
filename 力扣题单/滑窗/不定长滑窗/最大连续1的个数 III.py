class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        ans=0
        cnt=0
        for r,c in enumerate(nums):
            if c==0:
                cnt+=1
            while cnt>k:
                if nums[l]==0:
                    cnt-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans