class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        pre=[0]*n
        sur=[0]*n
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i]=max(nums[i],pre[i-1])
        sur[n-1]=nums[-1]
        for i in range(n-2,-1,-1):
            sur[i]=max(nums[i],sur[i+1])
        for i in range(1,n-1):
            temp=(pre[i-1]-nums[i])*sur[i+1]
            ans=max(ans,temp)
        return ans