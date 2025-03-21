class UnionFind:
    def __init__(self):
        self.father={}
        self.ans=0
    def find(self,x):
        root=x
        while self.father[root] is not None:
            root=self.father[root]
        while x!=root:
            original_father=self.father[x]
            self.father[x]=root
            x=original_father
        return root
    def merge(self,x,y):
        root_x,root_y=self.find(x),self.find(y)
        if root_x!=root_y:
            self.father[root_x]=root_y
            self.ans-=1

    def add(self,x):
        if x not in self.father:
            self.father[x]=None
            self.ans+=1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf=UnionFind()
        n=len(isConnected)
        for i in range(n):
            uf.add(i)
            for j in range(i):
                if isConnected[i][j]==1:
                    uf.merge(i,j)
        return uf.ans