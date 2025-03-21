class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a=low%2
        b=high%2
        s=a+b
        c=high-low-1
        if s==0:
            return c//2+1
        elif s==1:
            return c//2
        else:
            return c//2

