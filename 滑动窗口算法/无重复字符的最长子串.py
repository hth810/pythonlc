class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window={}
        left=0
        res=0
        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1
            while window[c]>1:
                window[s[left]]-=1
                left+=1
            res=max(res,r-left+1)
        return res