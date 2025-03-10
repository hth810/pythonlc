from collections import defaultdict


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        ans=0
        pre_xor=defaultdict(int)
        pre_xor[0]=1
        cur=0
        for i in nums:
            cur^=i
            ans+=pre_xor[cur]
            pre_xor[cur]+=1
        return ans