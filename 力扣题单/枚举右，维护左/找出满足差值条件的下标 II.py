class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n=len(nums)
        mn=mx=0
        for i in range(indexDifference,n):
            j=i-indexDifference
            if nums[j]>nums[mx]:
                mx=j
            elif nums[j]<nums[mn]:
                mn=j
            if abs(nums[i]-nums[mn])>=valueDifference:
                return [mn,i]
            if abs(nums[i]-nums[mx])>=valueDifference:
                return [mx,i]
        return [-1,-1]