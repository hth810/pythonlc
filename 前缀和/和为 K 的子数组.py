class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans,s=0,0
        from collections import defaultdict
        d=defaultdict(int)
        d[0]=1
        for i in nums:
            s+=i
            ans+=d[s-k]
            d[s]+=1
        return ans