import math

MOD=10**9+7
M_N=10**4
FACTORS=[[] for _ in range(M_N+1)]
for x in range(2,len(FACTORS)):
    t=x
    i=2
    while i*i<=t:
        e=0
        while t%i==0:
            e+=1
            t//=i
        if e:
            FACTORS[x].append(e)
        i+=1
    if t>1:
        FACTORS[x].append(1)

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans=0
        for a in range(1,maxValue+1):
            res=1
            for f in FACTORS[a]:
                res=res*math.comb(n+f-1,f)%MOD
            ans+=res
        return ans%MOD