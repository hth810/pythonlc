from itertools import accumulate


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        pre=list(accumulate(differences))
        l,h=lower,upper
        for i,c in enumerate(pre):
            l=max(l,lower-c)
            h=min(h,upper-c)
        if l>h:
            return 0
        return h-l+1