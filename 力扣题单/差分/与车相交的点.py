from itertools import accumulate


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        n=max(end for _,end in nums)
        ans=0
        diff=[0]*(n+2)
        for do,up in nums:
            diff[do]+=1
            diff[up+1]-=1
        for i in accumulate(diff):
            if i!=0:
                ans+=1
        return ans