from collections import Counter


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans=0
        temp=sum(nums[:k-1])
        cnt=Counter(nums[:k-1])
        for out,In in zip(nums,nums[k-1:]):
            temp+=In
            cnt[In]=cnt.get(In,0)+1
            if len(cnt)==k:
                ans=max(ans,temp)
            temp-=out
            cnt[out]-=1
            if cnt[out]==0:
                del cnt[out]
        return ans