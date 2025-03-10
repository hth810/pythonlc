class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n=len(s)
        cnt=0
        l=0
        ans=0
        if n==1:
            return 1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cnt+=1
            while cnt>1:
                if s[l]==s[l+1]:
                    cnt-=1
                l+=1
            ans=max(ans,i-l+1)
        return ans