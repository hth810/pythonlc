from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=defaultdict(int)
        ans,s=0,0
        cnt[0]=1
        for i,c in enumerate(nums):
            s+=c
            ans+=cnt[s-k]
            cnt[s]+=1
        return ans