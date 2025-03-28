from collections import defaultdict


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt=defaultdict(int)
        ans=0
        n=len(nums)
        for i in range(1,n-2):
            for j in range(i):
                cnt[nums[i]+nums[j]]+=1
            for j in range(i+2,n):
                ans+=cnt[nums[j]-nums[i+1]]
        return ans