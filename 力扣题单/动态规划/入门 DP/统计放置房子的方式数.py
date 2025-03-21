MOD=10**9+7
f=[1,2]
for _ in range(10**4-1):
    f.append((f[-1]+f[-2])%MOD)
class Solution:
    def countHousePlacements(self, n: int) -> int:
        return pow(f[n],2)%MOD