from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        s=defaultdict(list)
        for u,v in edges:
            s[u].append(v)
            s[v].append(u)
        vis=set()
        def dfs(i):
            if i==destination:
                return True
            vis.add(i)
            for j in s[i]:
                if j not in vis and dfs(j):
                    return True
            return False
        return dfs(source)