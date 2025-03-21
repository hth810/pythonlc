from collections import Counter


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        s=sum(nums)
        ans=float('-inf')
        for i in nums:
            cnt[i]-=1
            if (s-i)%2==0 and cnt[(s-i)//2]>0:
                ans=max(ans,i)
            cnt[i]+=1
        return ans