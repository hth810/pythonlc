import heapq
from itertools import pairwise


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for pre,cur in pairwise(grid):
            mn,mn2=heapq.nsmallest(2,pre)
            for j,k in enumerate(pre):
                cur[j]+=mn if k !=mn else mn2
        return min(grid[-1])