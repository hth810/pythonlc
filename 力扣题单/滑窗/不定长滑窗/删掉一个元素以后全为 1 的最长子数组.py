class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window={}
        n=len(nums)
        left=0
        res=0
        window[0]=0
        window[1]=0
        for i,c in enumerate(nums):
            window[c]+=1
            while window[0]>1:
                window[nums[left]]-=1
                left+=1
            res=max(res,i-left+1)
        return res-1