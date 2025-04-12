class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n=len(nums)
        pre=[float('inf')]*n
        sur=[float('inf')]*n
        for i in range(1,n):
            pre[i]=min(pre[i-1],nums[i-1])
        for j in range(n-2,-1,-1):
            sur[j]=min(sur[j+1],nums[j+1])
        ans=float('inf')
        for i in range(1,n-1):
            if nums[i]>pre[i] and nums[i]>sur[i]:
                ans=min(ans,nums[i]+pre[i]+sur[i])
        return -1 if ans==float('inf') else ans