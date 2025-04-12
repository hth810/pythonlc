class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n=len(s)
        pre=[0]*n
        for i in range(n-2,0,-1):
            pre[i]=pre[i+1] | (1<<(ord(s[i+1])-ord('a')))
        cur=1<<(ord(s[0])-ord('a'))
        ans=set()
        for i in range(1,n-1):
            temp=cur&pre[i]
            for j in range(26):
                if (temp>>j)&1:
                    ans.add(chr(j+97)+s[i])

            cur|=1<<(ord(s[i])-97)
        return len(ans)
