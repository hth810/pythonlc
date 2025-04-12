class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n=len(nums)
        pre=[0]*(n+1)
        for i in range(1,n+1):
            pre[i]=pre[i-1]+nums[i-1]

        a,b=max(pre),min(pre)
        return abs(a-b)