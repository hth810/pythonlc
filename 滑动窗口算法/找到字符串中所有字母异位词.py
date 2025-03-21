from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need=Counter(p)
        cnt={}
        ans=[]
        valid=0
        l=0
        for r,c in enumerate(s):
            if c in need:
                cnt[c]=cnt.get(c,0)+1
                if cnt[c]==need[c]:
                    valid+=1
            while valid == len(need):
                if r-l+1==len(p):
                    ans.append(l)
                d=s[l]
                l += 1
                if d in cnt:
                    if cnt[d]==need[d]:
                        valid-=1
                    cnt[d]-=1
                    if cnt[d]==0:
                        del cnt[d]
        return  ans