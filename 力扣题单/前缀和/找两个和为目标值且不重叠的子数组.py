from itertools import accumulate


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        pre=[float('inf')]*(n+1)
        l=0
        res=float('inf')
        s=[0]+list(accumulate(arr))
        for r in range(n):
            while s[r+1]-s[l]>target:
                l+=1
            if s[r+1]-s[l]==target:
                res=min(res,pre[l]+r+1-l)
                pre[r+1]=min(pre[r],r+1-l)
            else:
                pre[r+1]=pre[r]
        return -1 if res==float('inf') else res