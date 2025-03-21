class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        parent=list(range(n))
        size=[1]*n
        for x,y in edges:
            rx,ry=find(x),find(y)
            if rx!=ry:
                if size[rx]<size[ry]:
                    parent[rx]=ry
                    size[ry]+=size[rx]
                else:
                    parent[ry]=rx
                    size[rx]+=size[ry]

        return sum(n-size[find(x)] for x in range(n))//2