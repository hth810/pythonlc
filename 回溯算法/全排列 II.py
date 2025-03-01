class Solution:
    def __init__(self):
        self.res=[]

    def traverse(self,nums,track,used):
        if len(track)==len(nums):
            self.res.append(track.copy())
            return
        for i in range(len(nums)):
            if used[i]==1:
                continue
            if i>0 and nums[i]==nums[i-1] and used[i-1]==0:
                continue
            track.append(nums[i])
            used[i]=1
            self.traverse(nums,track,used)
            track.pop()
            used[i]=0
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        track=[]
        nums.sort()
        used=[0]*len(nums)
        self.traverse(nums,track,used)
        return self.res
