from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window={}
        need=Counter(t)
        length=float('inf')
        start=0
        valid=0
        l=0
        for r,c in enumerate(s):
            if c in need:
                window[c]=window.get(c,0)+1
                if window[c]==need[c]:
                    valid+=1
            while valid==len(need):
                if r-l+1<length:
                    start=l
                    length=r-l+1
                d=s[l]
                if d in need:
                    if window[d]==need[d]:
                        valid-=1
                    window[d]-=1
                l+=1
        return "" if length==float('inf') else s[start:start+length]
