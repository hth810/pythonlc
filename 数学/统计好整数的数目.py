import math
from collections import Counter


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        fac=[math.factorial(i) for i in range(n+1)]
        base=pow(10,(n-1)//2)
        s=set()
        ans=0
        for i in range(base,base*10):
            l=str(i)
            l+=l[::-1][n%2:]
            if int(l)%k:
                continue
            sa=''.join(sorted(l))
            if sa in s:
                continue
            s.add(sa)
            cnt=Counter(sa)
            res=(n-cnt['0'])*fac[n-1]
            for c in cnt.values():
                res//=fac[c]
            ans+=res
        return ans
