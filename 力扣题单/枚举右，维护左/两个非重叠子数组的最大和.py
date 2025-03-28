from itertools import accumulate


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n=len(nums)
        pre=[0]+list(accumulate(nums))
        ans=0
        def f(a,b):
            nonlocal ans
            ma=0
            for i in range(a+b,n+1):
                ma=max(ma,pre[i-b]- pre[i-a-b])
                ans=max(ans,ma+pre[i]-pre[i-b])
        f(firstLen,secondLen)
        f(secondLen,firstLen)
        return ans