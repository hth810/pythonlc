class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        pre=[0]*n
        sur=[0]*n
        ans=0
        for i in range(1,n):
            pre[i]=max(pre[i-1],nums[i-1])
        for i in range(n-2,-1,-1):
            sur[i]=max(sur[i+1],nums[i+1])

        for i in range(1,n-1):
            ans=max(ans,(pre[i]-nums[i])*sur[i])
        return ans
