class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt0=cnt1=0
        for i,x in enumerate(nums):
            nums[i]=2
            if x<=1:
                nums[cnt1]=1
                cnt1+=1
            if x==0:
                nums[cnt0]=1
                cnt0+=1

        """
        Do not return anything, modify nums in-place instead.
        """
