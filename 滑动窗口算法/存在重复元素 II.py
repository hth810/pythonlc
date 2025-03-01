class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        fast, slow = 0, 0
        hasBeem={}
        while fast<len(nums):
            c=nums[fast]
            fast+=1
            hasBeem[c]=hasBeem.get(c,0)+1
            if hasBeem[c] > 1:
                return True
            if fast-slow>k:
                d=nums[slow]
                slow+=1
                hasBeem[d]-=1

        return False

