from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt=defaultdict(int)
        l=0
        ans=0
        for r,c in enumerate(s):
            cnt[c]+=1
            while len(cnt)==3:
                d=s[l]
                cnt[d]-=1
                if cnt[d]==0:
                    del cnt[d]
                l+=1
            ans+=l
        return ans