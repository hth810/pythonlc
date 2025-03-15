class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n=len(nums)
        pre=[0]*(n+1)
        sur=[max(nums)]*(n+1)
        for i in range(1,n+1):
            pre[i]=max(pre[i-1],nums[i-1])
        for j in range(n-2,-1,-1):
            sur[j]=min(sur[j+1],nums[j+1])

        cnt=0
        for i in range(1,n-1):
            if pre[i]<nums[i]<sur[i]:
                cnt+=2
            elif nums[i-1]<nums[i]<nums[i+1]:
                cnt+=1
        return cnt
