from functools import cache


class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        def cost(a: str, b: str) -> int:
            diff = abs(ord(a) - ord(b))
            return min(diff, 26 - diff)
        @cache
        def dp(i: int, j: int, r: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1
            res = max(dp(i+1, j, r), dp(i, j-1, r))
            c = cost(s[i], s[j])
            if r >= c:
                res = max(res, 2 + dp(i+1, j-1, r - c))
            return res
        return dp(0, n-1, k)