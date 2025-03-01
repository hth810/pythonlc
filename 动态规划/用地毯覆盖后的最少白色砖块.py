from functools import cache


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        floor=list(map(int,floor))
        n=len(floor)
        @cache
        def dfs(num,i):
            if i<num*carpetLen:
                return 0
            if num==0:
                return dfs(num,i-1)+floor[i]
            return min(dfs(num-1,i-carpetLen),dfs(num,i-1)+floor[i])
        return dfs(numCarpets,n-1)
