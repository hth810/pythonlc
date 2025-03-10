class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        p=[0]*n
        for i in range(n):
            p[i]=abs(ord(s[i])-ord(t[i]))
        l=0
        ans=0
        cnt=0
        for r,c in enumerate(p):
            cnt+=c
            while cnt>maxCost:
                cnt-=p[l]
                l+=1
            ans=max(ans,r-l+1)
        return ans
