from collections import defaultdict


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        cnt=defaultdict(int)
        for rec in rectangles:
            temp=rec[0]/rec[1]
            cnt[temp]+=1
        ans=0
        for val in cnt.values():
            if val>=2:
                ans+=(val*(val-1))//2
        return ans