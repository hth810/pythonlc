from functools import cache


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        high=list(map(int,str(finish)))
        n=len(high)
        low=list(map(int,str(start).zfill(n)))
        diff=n-len(s)
        @cache
        def dfs(i,lli,uli):
            if i==n:
                return 1
            lo=low[i] if lli else 0
            up=high[i] if uli else 9
            res=0
            if i<diff:
                for d in range(lo,min(limit,up)+1):
                    res+=dfs(i+1,lli and d==lo,uli and d==up)
            else:
                x=int(s[i-diff])
                if lo<=x<=up:
                    res=dfs(i+1,lli and x==lo,uli and x==up)
            return res
        return dfs(0,True,True)