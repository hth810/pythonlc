class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n=len(flowers)
        for i in range(n):
            flowers[i]=min(target,flowers[i])
        left_flowers=newFlowers-(target*n-sum(flowers))
        if left_flowers==newFlowers:
            return n*full
        if left_flowers>=0:
            return max(partial*(target-1)+full*(n-1),full*n)
        pre=ans=j=0
        flowers.sort()
        for i in range(1,n+1):
            left_flowers+=target-flowers[i-1]
            if left_flowers<0:
                continue
            while j<i and flowers[j]*j<pre+left_flowers:
                pre+=flowers[j]
                j+=1
            avg=(left_flowers+pre)//j
            total=avg*partial+full*(n-i)
            ans=max(ans,total)
        return ans