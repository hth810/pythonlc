class SegmentTree:
    def __init__(self,a:[int]):
        n=len(a)
        self.max=[0]*(n*4)
        self.build(a,1,0,n-1)

    def maintain(self,o:int):
        self.max[o]=max(self.max[o*2],self.max[o*2+1])

    def build(self,a:[int],o:int,l:int,r:int):
        if l==r:
            self.max[o]=a[l]
            return
        m=(l+r)//2
        self.build(a,o*2,l,m)
        self.build(a,o*2+1,m+1,r)
        self.maintain(o)

    def update(self,o:int,l:int,r:int,i:int,x:int):
        if l==r:
            self.max[o]=x
            return
        m=(l+r)//2
        if i<=m:
            self.update(o*2,l,m,i,x)
        else:
            self.update(o*2+1,m+1,r,i,x)
        self.maintain(o)
        return i
    def find_first(self,o:int,l:int,r:int,x:int):
        if self.max[o]<x:
            return -1
        if l==r:
            return l
        m=(l+r)//2
        i=self.find_first(o*2,l,m,x)
        if i<0:
            i=self.find_first(o*2+1,m+1,r,x)
        return i


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        t=SegmentTree(baskets)
        n=len(baskets)
        ans=0
        for x in fruits:
            i=t.find_first(1,0,n-1,x)
            if i<0:
                ans+=1
            else:
                t.update(1,0,n-1,i,-1)
        return ans
