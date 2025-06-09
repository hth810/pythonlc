class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s=list('L'+dominoes+'R')
        pre=0
        for i,c in enumerate(s):
            if c=='.':
                continue
            if c==s[pre]:
                s[pre+1:i]=c*(i-pre-1)
            elif c=='L':
                m=(pre+i-1)//2
                s[pre+1:m+1]='R'*(m-pre)
                m=(pre+i)//2+1
                s[m:i]='L'*(i-m)
            pre=i
        return ''.join(s[1:-1])