class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        pa=list(range(n))
        size=[1]*n
        def find(x):
            if pa[x]!=x:
                pa[x]=find(pa[x])
            return pa[x]

        for x,y in connections:
            a,b=find(x),find(y)
            if a!=b:
                if size[a]<size[b]:
                    pa[a]=b
                    size[b]+=size[a]
                else:
                    pa[b]=a
                    size[a]+=size[b]
        return sum(pa[x]==x for x in range(n))-1