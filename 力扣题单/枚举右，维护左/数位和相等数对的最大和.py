from collections import defaultdict


class Solution:
    def c_n_t(self,n):
        s=0
        while n!=0:
            ge=n%10
            n=n//10
            s+=ge
        return s
    def maximumSum(self, nums: List[int]) -> int:
        cnt=defaultdict(list)
        ans=-1
        for i in nums:
            cnt[self.c_n_t(i)].append(i)
        for i,j in cnt.items():
            if len(j)>=2:
                j.sort()
                ans=max(ans,j[-1]+j[-2])
        return ans