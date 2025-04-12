from functools import cache


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        @cache
        def dfs(i):
            if i>=n:
                return 0
            return max(dfs(i+1),dfs(i+questions[i][1]+1)+questions[i][0])
        return dfs(0)