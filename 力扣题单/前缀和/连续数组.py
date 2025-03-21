from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if nums.count(0)==nums.count(1):
            return len(nums)
        cnt=defaultdict(lambda :-1)
        pre=0
        ans=0
        for i,c in enumerate(nums):
            if c==0:
                pre-=1
            else:
                pre+=1
            if cnt[pre]>=0:
                ans=max(ans,i-cnt[pre])
            else:
                cnt[pre]=i
            if pre==0:
                ans=max(ans,i+1)
        return ans