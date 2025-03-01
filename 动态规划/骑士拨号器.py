from functools import cache

MOD=10**9+7
NEXT=(4,6),(6,8),(7,9),(4,8),(3,9),(),(0,1,7),(2,6),(1,3),(2,4)

@cache
def dfs(i,j):
    if i==0:
        return 1
    return sum(dfs(i-1,k) for k in NEXT[j])%MOD

class Solution:
    def knightDialer(self, n: int) -> int:
        if n==1:
            return 10
        return (sum(dfs(n-1,i) for i in range(10)))%MOD
