from functools import cache


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n=len(s)
        @cache
        def judge(a,b):
            if a>=b:
                return True
            return s[a]==s[b] and judge(a+1,b-1)
        @cache
        def dfs(i,c):
            if c==0:
                return 1 if judge(0,i) else 0
            if i<0 and c>0:
                return 0
            res=0
            for j in range(1,i+1):
                if judge(j,i):
                    res=max(res,dfs(j-1,c-1))
            return res
        return dfs(n-1,2)==1

