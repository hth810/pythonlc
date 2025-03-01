from functools import cache


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        @cache
        def dfs(mouse, cat, turn):
            if mouse == 0:
                return 1
            if mouse == cat:
                return 2
            if turn>= 2*n*(n-1):
                return 0
            if turn%2 == 0:
                ping=0
                for new_mouse in graph[mouse]:
                    res = dfs(new_mouse, cat, turn+1)
                    if res == 1:
                        return 1
                    elif res == 0:
                        ping = 1
                return 0 if ping else 2
            else:
                ping=0
                for new_cat in graph[cat]:
                    if new_cat == 0:
                        continue
                    res= dfs(mouse, new_cat, turn+1)
                    if res == 2:
                        return 2
                    if res == 0:
                        ping = 1
                return 0 if ping else 1
        return dfs(1, 2, 0)