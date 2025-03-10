class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n=len(nums)
        s=sum(nums)
        tgt=s-x
        if tgt<0:
            return -1
        if tgt==0:
            return n
        l=0
        ans=0
        cnt=0
        for r,c in enumerate(nums):
            cnt+=c
            while cnt>tgt and l<r:
                cnt-=nums[l]
                l+=1

            if cnt==tgt:
                ans=max(ans,r+1-l)

        return -1 if ans==0 else n-ans