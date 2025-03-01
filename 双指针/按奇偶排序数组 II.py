class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ou,ji=0,1
        n=len(nums)
        while True:
            if nums[ou]%2==0:
                ou+=2
                
            if nums[ji]%2==1:
                ji+=2
            if ou > n - 2:
                break
            if ji > n - 1:
                break
            if nums[ou]%2==1 and nums[ji]%2==0:
                nums[ji],nums[ou]=nums[ou],nums[ji]
                ji+=2
                ou+=2
            if ou > n - 2:
                break
            if ji > n - 1:
                break
        return nums