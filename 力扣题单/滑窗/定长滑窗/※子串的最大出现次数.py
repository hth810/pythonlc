from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ans=0
        cnt=defaultdict(int)
        temp=''
        for i,c in enumerate(s):
            temp+=c
            if i<minSize-1:
                continue
            if len(set(temp))<=maxLetters:
                cnt[temp]+=1
            temp=temp[1:]
        return max(cnt.values()) if cnt else 0