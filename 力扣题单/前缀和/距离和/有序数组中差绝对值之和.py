from itertools import accumulate


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre=[0]+list(accumulate(nums))
        n=len(nums)
        sur=[0]*(n+1)
        for i in range(n-2,-1,-1):
            sur[i]=sur[i+1]+nums[i+1]
        ans=[]
        for i in range(n):
            t=i*nums[i]-pre[i]+sur[i]-nums[i]*(n-i-1)
            ans.append(t)
        return ans
