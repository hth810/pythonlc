class FenwickTree:
    def __init__(self,n):
        self.tree=[0]*(n+1)
    def update(self,i,val):
        while i<len(self.tree):
            self.tree[i]+=val
            i+=i&-i
    def pre(self,i):
        res=0
        while i>0:
            res+=self.tree[i]
            i-=i&-i
        return res
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        p=[0]*n
        for i,c in enumerate(nums1):
            p[c]=i
        ans=0
        t=FenwickTree(n)
        for i,x in enumerate(nums2):
            x=p[x]
            less=t.pre(x)
            ans+=less*(n-1-x-(i-less))
            t.update(x+1,1)
        return ans