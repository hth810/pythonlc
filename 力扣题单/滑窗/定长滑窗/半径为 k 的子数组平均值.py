class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        m=k*2+1
        res=[-1]*n
        temp=0
        for i,c in enumerate(nums):
            temp+=c
            if i<m-1:
                continue
            res[i-k]=temp//m
            temp-=nums[i-m+1]
        return res