from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pos=nums.index(k)
        cnt=defaultdict(int)
        cnt[0]=1
        temp=0
        for i in range(pos-1,-1,-1):
            temp+=1 if nums[i]<k else -1
            cnt[temp]+=1
        ans=cnt[0]+cnt[-1]
        temp=0
        for i in range(pos+1,n):
            temp+=1 if nums[i]>k else -1
            ans+=cnt[temp]+cnt[temp-1]
        return ans