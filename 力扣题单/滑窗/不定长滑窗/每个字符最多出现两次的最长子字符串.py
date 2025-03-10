class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        window={}
        left=0
        res=0
        for r,c in enumerate(s):
            window[c]=window.get(c,0)+1
            while window[c]>2:
                window[s[left]]-=1
                left+=1
            res=max(res,r-left+1)
        return res