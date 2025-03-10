from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        cnt=defaultdict(int)
        ans=0
        for r,c in enumerate(nums):
            cnt[c]+=1
            while cnt[c]>k:
                cnt[nums[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans


