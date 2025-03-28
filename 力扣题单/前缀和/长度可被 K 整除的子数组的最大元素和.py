from collections import defaultdict
from itertools import accumulate


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pre=[0]+list(accumulate(nums))
        ans=float('-inf')
        cnt=defaultdict(lambda :float('inf'))
        for i,c in enumerate(pre):
            a=i%k
            ans=max(ans,c-cnt[a])
            cnt[a]=min(cnt[a],c)
        return ans