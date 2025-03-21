import math


class Solution:
    def minSwaps(self, s: str) -> int:
        stack=0
        n=len(s)
        cnt=0
        for i,c in enumerate(s):
            if c=='[':
                stack+=1
            elif c==']' and stack>0:
                stack-=1
            else:
                cnt+=1

        return math.ceil(cnt/2)