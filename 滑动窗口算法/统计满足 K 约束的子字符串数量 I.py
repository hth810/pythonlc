class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left, right = 0, 0
        one, zero=0,0
        res=0
        while right<len(s):
            if s[right]=='1':
                one+=1
            else:
                zero+=1
            while one>k and zero>k and left<=right:
                if s[left]=='1':
                    one-=1
                else:
                    zero-=1
                left+=1
            res+=right-left+1
            right+=1
        return res