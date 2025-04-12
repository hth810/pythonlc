class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        n=len(candiesCount)
        pre=[0]*(n+1)
        for i in range(1,n+1):
            pre[i]=candiesCount[i-1]+pre[i-1]
        res=[]
        for typ,day,m in queries:
            tem_m=m*(day+1)
            tem_l=day+1
            mi=pre[typ]+1
            ma=pre[typ]+candiesCount[typ]
            res.append(tem_l<=ma and tem_m>=mi)
        return res