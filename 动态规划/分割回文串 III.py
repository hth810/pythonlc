from functools import cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n=len(s)
        @cache
        def min_cost(i,j):
            if i>=j:
                return 0
            return min_cost(i+1,j-1)+(1 if s[i]!=s[j] else 0)
        @cache
        def dfs(i,r):
            if i==0:
                return min_cost(0,r)
            return min(dfs(i-1,l-1)+min_cost(l,r) for l in range(i,r+1))

        return dfs(k-1,n-1)