from collections import defaultdict


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        cnt=defaultdict(list)
        for x,y in connections:
            cnt[x].append(y)
            cnt[y].append(x)
        vis=set()
        def dfs(i):
            vis.add(i)
            for j in cnt[i]:
                if j not  in vis:
                    dfs(j)
        count=0
        for i in range(n):
            if i not in vis:
                dfs(i)
                count+=1

        return count-1
