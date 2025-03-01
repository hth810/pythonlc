from itertools import groupby

MOD=10**9+7
a=[1,1,2,4]
b=[1,1,2,4]
for _ in range(10**5-3):
    a.append((a[-1]+a[-2]+a[-3])%MOD)
    b.append((b[-1]+b[-2]+b[-3]+b[-4])%MOD)
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        ans=1
        for w,r in groupby(pressedKeys):
            n=len(list(r))
            ans=ans*(b[n] if w in '79' else a[n]) %MOD

        return ans