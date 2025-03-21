from collections import defaultdict


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        cnt=defaultdict(list)
        for x,y in edges:
            cnt[x].append(y)
            cnt[y].append(x)
        vis=set()
        def dfs(i):
            vis.add(i)
            size=1
            for j in cnt[i]:
                if j not in vis:
                    size+=dfs(j)
            return size
        ans=temp=0
        for i in range(n):
            if i not in vis:
                size=dfs(i)
                ans+=size*temp
                temp+=size
        return ans