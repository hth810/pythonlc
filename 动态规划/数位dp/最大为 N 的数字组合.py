from functools import cache


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s=str(n)
        @cache
        def f(i,is_limit,is_num):
            if i==len(s):
                return int(is_num)
            res=0
            if not is_num:
                res=f(i+1,False,False)
            up=s[i] if is_limit else '9'
            for d in digits:
                if d>up:
                    break
                res+=f(i+1,is_limit and d==up,True)
            return res
        return f(0,True,False)