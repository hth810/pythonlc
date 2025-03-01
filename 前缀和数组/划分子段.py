def maxSumAfterPartitioning(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        current_sum = 0
        for j in range(i, 0, -1):  # 从i向前找到最优的j
            current_sum += arr[i - j]
            dp[i] = max(dp[i], dp[i - j] + j * current_sum)
    return dp[n]

# 样例输入
n1 = 5
a1 = [10, 1, 2, 5, -3]
n2 = 4
a2 = [-1, -2, -3, -4]

# 输出结果
print(maxSumAfterPartitioning(a1))  # 样例输出 1: 26
print(maxSumAfterPartitioning(a2))  # 样例输出 2: -10