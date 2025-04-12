from collections import defaultdict


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n=len(nums)
        pre=[0]*(n+1)
        for i in range(1,n+1):
            pre[i]=(nums[i-1]+pre[i-1])%p
        tgt=pre[-1]%p
        if tgt==0:
            return 0
        cnt=defaultdict(int)
        ans=float('inf')
        for i,c in enumerate(pre):
            if (c-tgt+p)%p in cnt:
                ans=min(ans,i-cnt[(c-tgt+p)%p])
            cnt[c]=i
        return -1 if ans==n else ans