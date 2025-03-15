class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow=fast=0
        n=len(nums)
        while fast<n:
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        for i in range(slow,n):
            nums[i]=0
        """
        Do not return anything, modify nums in-place instead.
        """
