from collections import Counter

MOD=10**9+7
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        lst = [0] * 26
        for k, v in Counter(s).items():
            lst[ord(k) - 97] = v
        for _ in range(t):
            lst = [lst[-1], (lst[-1] + lst[0]) % MOD] + lst[1: -1]
        return sum(lst) % MOD