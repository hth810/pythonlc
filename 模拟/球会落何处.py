class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [-1] * n
        for j in range(n):
            cur = j
            for row in grid:
                d = row[cur]
                cur += d
                if cur< 0 or cur== n or row[cur] != d:
                    break
            else:
                ans[j] = cur
        return ans
