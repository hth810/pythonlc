class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans=0
        mni=mxi=i0=-1
        for i,c in enumerate(nums):
            if c==minK:
                mni=i
            if c==maxK:
                mxi=i
            if not minK<=c<=maxK:
                i0=i
            ans+=max(min(mni,mxi)-i0,0)
        return ans