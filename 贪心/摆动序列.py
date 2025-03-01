class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        pre=0
        suf=0
        res=1
        for i in range(0,len(nums)-1):
            suf=nums[i+1]-nums[i]
            if (pre<=0 and suf>0) or (pre>=0 and suf<0):
                res+=1
                pre=suf
        return res