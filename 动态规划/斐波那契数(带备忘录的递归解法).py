class Solution:
    def dp(self,memo: List[int], n: int) -> int:
        if n == 0 or n == 1: return n
        if memo[n] != 0: return memo[n]
        memo[n] = self.dp(memo, n - 1) + self.dp(memo, n - 2)
        return memo[n]
    def fib(self, n: int) -> int:
        memo = [0] * (n + 1)
        return self.dp(memo, n)
