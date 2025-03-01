class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        ans=0
        cnts=[[0]*11 for _ in range(n)]
        win=[False]*n
        for x,y in pick:
            cnts[x][y]+=1
            if not win[x] and cnts[x][y]>x:
                win[x]=True
                ans+=1
        return ans