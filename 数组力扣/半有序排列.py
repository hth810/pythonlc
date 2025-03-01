class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while nums[left]!=1 or nums[right]!=len(nums):
            if nums[left]!=1:
                left+=1
            if nums[right]!=len(nums):
                right-=1
        if right<left:
            return left+len(nums)-2-right
        else:
            return left+len(nums)-1-right