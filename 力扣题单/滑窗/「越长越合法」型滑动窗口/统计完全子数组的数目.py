from collections import defaultdict


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        tgt=len(set(nums))
        cnt=defaultdict(int)
        l=0
        ans=0
        for i,c in enumerate(nums):
            cnt[c]+=1
            while len(cnt)==tgt:
                d=nums[l]
                cnt[d]-=1
                if not cnt[d]:
                    del cnt[d]
                l+=1
            ans+=l
        return ans