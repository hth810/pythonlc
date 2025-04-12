MOD=10**9+7

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        s, d = [0] * (n + 1), [0] * n
        for i in range(n):
            s[i + 1] = s[i] + arr[i]
            d[i] = max(d[i - 1] + arr[i], 0)
        if k == 1:
            return max(d)
        return max(max(d), max(s[n], 0) * (k - 2) + s[n] - min(s) + max(s)) %MOD
