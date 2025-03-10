class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt={}
        for i,c in enumerate(nums):
            if target-c in cnt:
                return [cnt[target-c],i]
            cnt[c]=i