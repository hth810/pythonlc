class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        cnt={0}
        ans=temp=0
        for i,c in enumerate(nums):
            temp+=c
            if temp-target in cnt:
                temp=0
                ans+=1
                cnt={0}
            else:
                cnt.add(temp)
        return ans