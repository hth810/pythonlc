from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window=defaultdict(int)
        cnt=0
        ans=0
        l=0
        for r,c in enumerate(nums):
            cnt+=c
            window[c]+=1
            while window[c]>1:
                cnt-=nums[l]
                window[nums[l]]-=1
                l+=1
            ans=max(ans,cnt)
        return ans