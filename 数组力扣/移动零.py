class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        fast, slow = 0, 0
        l0=len(nums)
        while fast<l0:
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        for i in range(slow,l0):
            nums[i]=0
