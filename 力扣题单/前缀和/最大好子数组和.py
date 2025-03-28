from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pre=0
        ans=float('-inf')
        cnt=defaultdict(lambda :float('inf'))
        for c in nums:
            ans=max(ans,pre+c-min(cnt[c-k],cnt[c+k]))
            cnt[c]=min(pre,cnt[c])
            pre+=c

        return 0 if ans==float('-inf') else ans