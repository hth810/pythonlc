from functools import cache


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s=str(n)
        @cache
        def f(i,mask,is_limit,is_num):
            if i==len(s):
                return int(is_num)
            res=0
            if not is_num:
                res=f(i+1,mask,False,False)
            up=int(s[i]) if is_limit else 9
            for d in range(1-int(is_num),up+1):
                if mask >> d & 1 ==0:
                    res+=f(i+1,mask|(1<<d),is_limit and d==up, True)
            return res
        return f(0,0,True,False)