from collections import deque


class UnionFind:
    def __init__(self,n):
        self.pa=list(range(n))

    def find(self,x):
        if self.pa[x]!=x:
            self.pa[x]=self.find(self.pa[x])

        return self.pa[x]

    def merge(self,x,y):
        self.pa[self.find(x)]=self.find(y)
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        uf=UnionFind(n+2)
        uf.merge(p,p+2)
        for i in banned:
            uf.merge(i,i+2)
        q=deque([p])
        ans=[-1]*n
        ans[p]=0
        while q:
            i=q.popleft()
            mn=max(i-k+1,k-1-i)
            mx=min(i+k-1,2*n-k-i-1)
            j=uf.find(mn)
            while j<=mx:
                ans[j]=ans[i]+1
                q.append(j)
                uf.merge(j,j+2)
                j=uf.find(j+2)
        return ans