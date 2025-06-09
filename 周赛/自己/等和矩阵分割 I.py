class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        t = 0
        col = [0] * n
        for row in grid:
            for j in range(n):
                t+=row[j]
                col[j] += row[j]
        if t % 2 != 0:
            return False
        a = t // 2
        row = 0
        for i in range(m):
            row += sum(grid[i])
            if row == a:
                return True
            if row> a:
                break
        c = 0
        for j in range(n):
            c += col[j]
            if c == a:
                return True
            if c > a:
                break

        return False