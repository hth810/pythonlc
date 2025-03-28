from collections import defaultdict


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n=len(hours)
        ans=0
        pre=[0]*(n+1)
        cnt=defaultdict(lambda :-1)
        for i,c in enumerate(hours):
            if c>8:
                pre[i+1]=pre[i]+1
            else:
                pre[i+1]=pre[i]-1
        for i,c in enumerate(pre):
            if c>0:
                ans=max(ans,i)
            if cnt[c-1]!=-1:
                ans=max(ans,i-cnt[c-1])
            if cnt[c]==-1:
                cnt[c]=i
        return ans