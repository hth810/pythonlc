def count_partitions(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j - 1]
            if i >= j:
                dp[i][j] += dp[i - j][j]

    return dp[n][k]


n, k = map(int, input().split())

print(count_partitions(n, k))
