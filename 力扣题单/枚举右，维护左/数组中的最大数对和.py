from collections import defaultdict


class Solution:
    def f(self,n):
        a=0
        while n!=0:
            ge=n%10
            n=n//10
            a=max(a,ge)

        return a
    def maxSum(self, nums: List[int]) -> int:
        cnt=defaultdict(list)
        for i,c in enumerate(nums):
            cnt[self.f(c)].append(c)
        ans=-1
        for i,val in cnt.items():
            if len(val)>=2:
                val.sort()
                ans=max(ans,val[-1]+val[-2])

        return ans