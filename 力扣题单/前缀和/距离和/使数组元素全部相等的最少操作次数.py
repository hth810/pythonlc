from bisect import bisect_left
from itertools import accumulate


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        ans=[]
        s=[0]+list(accumulate(nums))
        for q in queries:
            i=bisect_left(nums,q)
            left=q*i-s[i]
            right=s[n]-s[i]-q*(n-i)
            ans.append(left+right)
        return ans