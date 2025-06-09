from functools import cache
MOD=10**9+7

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        @cache
        def dfs(i,c):
            if c<0:
                return 0
            if i<=0:
                return 1 if c==0 else 0
            if c<pow(i,x):
                return dfs(i-1,c)
            return (dfs(i-1,c)+dfs(i-1,c-pow(i,x)))%MOD
        return dfs(int(pow(n,1/x))+1,n)

