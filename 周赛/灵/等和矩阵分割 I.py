class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total=sum(sum(row) for row in grid)
        def check(matrix):
            s=0
            for a in matrix[:-1]:
                s+=sum(a)
                if s*2==total:
                    return True
            return False
        return check(grid) or check(list(zip(*grid)))
