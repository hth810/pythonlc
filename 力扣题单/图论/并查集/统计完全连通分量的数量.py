import math


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        pa=list(range(n))
        size=[1] * n
        edge=[0] * n
        def find(x):
            if pa[x]!=x:
                pa[x]=find(pa[x])
            return pa[x]
        for i,j in edges:
            ru=find(i)
            rv=find(j)
            if ru!=rv:
                if size[ru]<size[rv]:
                    ru,rv=rv,ru
                pa[rv]=ru
                size[ru]+=size[rv]
                edge[ru]+=edge[rv]+1
            else:
                edge[ru]+=1
        roots=set()
        for i in range(n):
            roots.add(find(i))
        ans=0
        for i in roots:
            if math.comb(size[i],2)==edge[i]:
                ans+=1
        return ans