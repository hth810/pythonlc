from functools import cache


class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        @cache
        def judge(a,b):
            if a>=b:
                return True
            return s[a]==s[b] and judge(a+1,b-1)
        @cache
        def dfs(r):
            if judge(0,r):
                return 0
            res=float('inf')
            for l in range(1,r+1):
                if judge(l,r):
                    res=min(res,dfs(l-1)+1)
            return res
        return dfs(n-1)
