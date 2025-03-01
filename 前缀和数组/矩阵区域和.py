class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1] + mat[i - 1][j - 1]
        answer = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x1, y1, x2, y2 = max(i - k, 0), max(j - k, 0), min(i + k, m - 1), min(j + k, n - 1)
                answer[i][j] = preSum[x2 + 1][y2 + 1] - preSum[x1][y2 + 1] - preSum[x2 + 1][y1] + preSum[x1][y1]
        return answer