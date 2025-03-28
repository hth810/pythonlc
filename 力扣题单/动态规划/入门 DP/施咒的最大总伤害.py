from collections import Counter
from functools import cache


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt=Counter(power)
        s=sorted(cnt.keys())
        n=len(s)
        @cache
        def dfs(i):
            if i<0:
                return 0
            x=s[i]
            j=i
            while j and s[j-1]>=x-2:
                j-=1
            return max(dfs(i-1),dfs(j-1)+x*cnt[x])
        return dfs(n-1)