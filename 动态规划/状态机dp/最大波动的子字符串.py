from itertools import permutations
from string import ascii_lowercase


class Solution:
    def largestVariance(self, s: str) -> int:
        ans = 0
        for a, b in permutations(ascii_lowercase, 2):
            f0, f1 = 0,float('-inf')
            for ch in s:
                if ch == a:
                    f0 = max(f0, 0) + 1
                    f1 += 1
                elif ch == b:
                    f1 = f0 = max(f0, 0) - 1
                ans = max(ans, f1)
        return ans