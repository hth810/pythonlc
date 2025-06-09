from functools import cache


class Solution:
    def change(self,n,base):
        digits = "0123456789"
        result = []

        while n > 0:
            n, remainder = divmod(n, base)
            result.append(digits[remainder])

        return ''.join(reversed(result))
    def countNumbers(self, l: str, r: str, b: int) -> int:
        r=self.change(int(r),b)
        l=self.change(int(l),b)
        r=list(map(int,r))
        n=len(r)
        l=list(map(int,l.zfill(n)))
        @cache
        def f(i,pre,lli,is_limit):
            if i==n:
                return 1
            res=0
            low=pre
            up=r[i] if is_limit else b-1
            if low>up:
                return 0
            for d in range(low,up+1):
                res+=f(i+1,d,is_limit and d==up)
            return res
        return f(0,0,True)