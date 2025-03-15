from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n=len(time)
        ans=0
        cnt=defaultdict(int)
        for i in range(n):
            temp=time[i]%60
            if cnt[(60-temp)%60]:
                ans+=cnt[(60-temp)%60]
            cnt[temp]+=1
        return ans
