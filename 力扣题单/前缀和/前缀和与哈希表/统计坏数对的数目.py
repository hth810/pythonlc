import math
from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        cnt=defaultdict(int)
        n=len(nums)
        ans=0
        for i,c in enumerate(nums):
            cnt[c-i]+=1
        for i in cnt.values():
            if i>1:
                ans+=math.comb(i,2)
        return math.comb(n,2)-ans
