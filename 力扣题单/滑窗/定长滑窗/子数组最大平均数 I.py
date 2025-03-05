class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=-(10**6)
        cnt=0
        for i,a in enumerate(nums):
            cnt+=a
            if i<k-1:
                continue
            ans=max(ans,cnt/k)
            cnt-=nums[i-k+1]
        return ans
