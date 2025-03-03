class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        cur=0
        nxt=0
        for i in range(n-1):
            nxt=max(nxt,i+nums[i])
            if i==cur:
                cur=nxt
                ans+=1

        return ans