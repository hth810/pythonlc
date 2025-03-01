class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]>=target:
                right=mid
            elif nums[mid]<target:
                left=mid+1
        return left
    def search1(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)#左闭右开
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        return left#right
    def search2(self, nums: List[int], target: int) -> int:
        left=-1
        right=len(nums)
        while left+1<right:
            mid=left+(right-left)//2
            if nums[mid]<target:
                left=mid
            else:
                right=mid
        return right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=self.search2(nums,target)
        if first==len(nums) or nums[first]!=target:
            return [-1,-1]
        last=self.search2(nums,target+1)-1
        return [first,last]
