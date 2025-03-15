class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n=len(nums)
        pre=[0]*(n+1)
        idx=[0]*n
        ans=0
        for i in range(1,n+1):
            pre[i]=pre[i-1]+nums[i-1]
            if i<n:
                idx[i]=max(0,i-nums[i])
        for i in range(n):
            ans+=pre[i+1]-pre[idx[i]]
        return ans