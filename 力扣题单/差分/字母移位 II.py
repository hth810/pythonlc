from itertools import accumulate


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        s=list(map(str,s))
        diff=[0]*(n+1)
        for i,j,k in shifts:
            a=1 if k==1 else -1
            diff[i]+=a
            diff[j+1]-=a
        diff=list(accumulate(diff))
        for i in range(n):
            if not diff[i]:
                continue
            t=diff[i]
            a=ord(s[i])-97
            temp=(a+t+26)%26
            s[i]=chr(temp+97)
        return ''.join(s)