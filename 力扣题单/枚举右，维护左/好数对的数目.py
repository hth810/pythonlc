from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt=defaultdict(int)
        ans=0
        for i in nums:
            cnt[i]+=1
        for val in cnt.values():
            if val>=2:
                ans+=(val*(val-1))//2

        return ans