from collections import defaultdict


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt=defaultdict(int)
        ans=0
        for i,c in enumerate(hours):
            a=c%24
            if cnt[(24-a)%24]!=0:
                ans+=cnt[(24-a)%24]
            cnt[a]+=1
        return ans