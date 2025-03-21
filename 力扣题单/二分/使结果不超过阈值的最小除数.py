class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        left=0
        right=max(nums)+1
        while left+1<right:
            mid=(left+right)//2
            if sum((x-1)//mid for x in nums)<=threshold-n:
                right=mid
            else:
                left=mid
        return right