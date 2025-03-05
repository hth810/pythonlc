class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        t=nums+nums
        k=nums.count(1)
        if k==1:
            return 0
        if k==0:
            return 0
        res=0
        temp=0
        for i,c in enumerate(t):
            if c==1:
                temp+=1
            if i<k-1:
                continue
            res=max(res,temp)
            if t[i-k+1]==1:
                temp-=1
        return k-res
