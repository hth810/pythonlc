from functools import cache
from itertools import accumulate


class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        pre=[0]+list(accumulate(nums))
        pre1=[0]+list(accumulate(cost))
        n=len(nums)
        @cache
        def dfs(i,r):
            if r==n:
                return 0
            res=0
            for j in range(r,n):
                res+=min(dfs(i+1,j+1))+(pre[j]-pre[r]+k*i)*(pre1[j]-pre1[r])
            return res
        return dfs(1,0)
