from functools import cache


def check(x,y):
    d=abs(ord(x)-ord(y))
    return d==1 or d==25
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n=len(s)
        @cache
        def emp(i,j):
            if i>j:
                return True
            if check(s[i],s[j]) and emp(i+1,j-1):
                return True
            for k in range(i+1,j-1,2):
                if emp(i,k) and emp(k+1,j):
                    return True
            return False

        @cache
        def dfs(i):
            if i==n:
                return ''
            res=s[i]+dfs(i+1)
            for j in range(i+1,n,2):
                if emp(i,j):
                    res=min(res,dfs(j+1))
            return res
        return dfs(0)