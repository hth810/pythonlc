from itertools import accumulate
from collections import defaultdict


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n=len(nums)
        for i in range(n):
            nums[i]=1 if nums[i]%modulo==k else 0
        a=[0]+list(accumulate(nums))
        cnt=defaultdict(int)
        ans=0
        for i,c in enumerate(a):
            ans+=cnt[(c-k+modulo)%modulo]
            cnt[c%modulo]+=1
        return ans


