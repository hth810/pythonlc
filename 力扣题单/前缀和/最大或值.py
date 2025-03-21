class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        a=pow(2,k)
        ans=0
        n=len(nums)
        pre=[0]*n
        sur=[0]*n
        for i in range(1,n):
            pre[i]=pre[i-1] | nums[i-1]
        for j in range(n-2,-1,-1):
            sur[j]=sur[j+1] | nums[j+1]
        for i,c in enumerate(nums):
            ans=max(ans,pre[i] | c*a | sur[i])

        return ans