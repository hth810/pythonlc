from itertools import accumulate


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        n=max(end for _,end in ranges)
        if left>n or right>n:
            return False
        diff=[0]*(n+2)
        f=[0]*(n+2)
        for down,up in ranges:
            diff[down]+=1
            diff[up+1]-=1
        f[0]=diff[0]
        for i in range(1,n+2):
            f[i]=f[i-1]+diff[i]
        for i in f[left:right+1]:
            if i==0:
                return False

        return True
