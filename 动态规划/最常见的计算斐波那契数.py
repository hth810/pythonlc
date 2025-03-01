def fib(n: int) -> int:
    if n == 0 or n == 1:
        # base case
        return n
    # 分别代表 dp[i - 1] 和 dp[i - 2]
    dp_i_1, dp_i_2 = 1, 0
    for i in range(2, n + 1):
        # dp[i] = dp[i - 1] + dp[i - 2];
        dp_i = dp_i_1 + dp_i_2
        # 滚动更新
        dp_i_2 = dp_i_1
        dp_i_1 = dp_i
    return dp_i_1