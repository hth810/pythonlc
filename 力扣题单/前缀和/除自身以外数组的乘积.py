class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[1]*n
        sur=[1]*n
        ans=[]
        for i in range(1,n):
            pre[i]=nums[i-1]*pre[i-1]
        for i in range(n-2,-1,-1):
            sur[i]=nums[i+1]*sur[i+1]
        for i in range(n):
            ans.append(pre[i]*sur[i])
        return ans