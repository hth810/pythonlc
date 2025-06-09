from bisect import bisect_right
from collections import defaultdict


class Solution:
    def maxSubstrings(self, word: str) -> int:
        cnt=defaultdict(list)
        for i,c in enumerate(word):
            cnt[c].append(i)
        tmp=[]
        for c in cnt:
            pos=cnt[c]
            n=len(pos)
            for j in range(n):
                cur=pos[j]
                i=bisect_right(pos,cur-3,0,j)-1
                if i>=0:
                    st=pos[i]
                    e=cur
                    if e-st+1>=4:
                        tmp.append((st,e))
        tmp.sort(key=lambda x:x[1])
        res=0
        l=-1
        for m,n in tmp:
            if m>l:
                res+=1
                l=n
        return res
