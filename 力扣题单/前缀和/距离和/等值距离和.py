from collections import defaultdict
from itertools import accumulate


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n=len(nums)
        cnt=defaultdict(list)
        for i,c in enumerate(nums):
            cnt[c].append(i)
        ans=[0]*n
        for a in cnt.values():
            s=[0]+list(accumulate(a))
            e=len(a)
            for j,tgt in enumerate(a):
                left=tgt*j-s[j]
                right=s[e]-s[j]-tgt*(e-j)
                ans[tgt]=left+right
        return ans
