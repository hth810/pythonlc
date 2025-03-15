class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=cur=nums[0]
        for i in nums[1:]:
            cur=max(i,cur+i)
            ans=max(cur,ans)
        return ans