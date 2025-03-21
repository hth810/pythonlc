from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt=defaultdict(int)
        ans=s=0
        cnt[0]=1
        for i,c in enumerate(nums):
            s+=c
            ans+=cnt[s-goal]
            cnt[s]+=1
        return ans