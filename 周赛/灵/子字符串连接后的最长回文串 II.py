class Solution:
    def calc(self,s,t):
        n, m = len(s), len(t)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i,x in enumerate(s):
            for j,y in enumerate(t):
                if x==y:
                    f[i+1][j]=f[i][j+1]+1
        mx = list(map(max, f))
        ans = max(mx) * 2
        for i in range(2*n-1):
            l,r=i//2,(i+1)//2
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if l+1<=r-1:
                ans=max(ans,r-l-1+mx[l+1]*2)
        return ans
    def longestPalindrome(self, s: str, t: str) -> int:
        return max(self.calc(s,t),self.calc(t[::-1],s[::-1]))

