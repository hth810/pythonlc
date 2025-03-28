from collections import defaultdict
MOD=10**9+7

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        cnt=defaultdict(int)
        ans=0
        for i in nums:
            temp=i-int(str(i)[::-1])
            ans+=cnt[temp]%MOD
            cnt[temp]+=1
        return ans%MOD