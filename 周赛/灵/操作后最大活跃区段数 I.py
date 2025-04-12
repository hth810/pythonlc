from itertools import groupby


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        mx=0
        pre=float('-inf')
        ans=0
        for i,c in groupby(s):
            cnt=len(list(c))
            if i=='1':
                ans+=cnt
            else:
                mx=max(mx,pre+cnt)
                pre=cnt
        return ans+mx