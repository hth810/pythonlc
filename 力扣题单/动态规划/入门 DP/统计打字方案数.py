from functools import cache
from itertools import groupby


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD=10**9+7
        ans=1
        @cache
        def dfs1(i):
            if i<0:
                return 0
            if i==0:
                return 1
            return (dfs1(i-1)+dfs1(i-2)+dfs1(i-3))%MOD
        @cache
        def dfs2(i):
            if i<0:
                return 0
            if i==0:
                return 1
            return (dfs2(i-1)+dfs2(i-2)+dfs2(i-3)+dfs2(i-4))%MOD
        for k,s in groupby(pressedKeys):
            n=len(list(s))
            ans=ans*(dfs2(n) if k in'79' else dfs1(n))%MOD

        return ans