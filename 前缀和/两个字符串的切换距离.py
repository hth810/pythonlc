class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        SIGMA=26
        nxt=[0]*(SIGMA*2+1)
        prv=[0]*(SIGMA*2+1)
        for i in range(SIGMA*2):
            nxt[i+1]=nxt[i]+nextCost[i%SIGMA]
            prv[i+1]=prv[i]+previousCost[i%SIGMA]

        ans=0
        for x,y in zip(s,t):
            x=ord(x)-ord('a')
            y=ord(y)-ord('a')
            ans+=min(nxt[y+SIGMA if x>y else y]-nxt[x],
                     prv[(x+SIGMA if x<y else x)+1]-prv[y+1])
        return ans