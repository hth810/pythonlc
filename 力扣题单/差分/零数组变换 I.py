from itertools import accumulate


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n=len(nums)
        diff=[0]*n
        for a,b in queries:
            diff[a]+=1
            if b<n-1:
                diff[b+1]-=1
        pre=list(accumulate(diff))
        return all(nums[i]<=pre[i] for i in range(n))