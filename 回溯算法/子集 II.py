class Solution:
    def __init__(self):
        self.res=[]
    def traverse(self,nums,start,track):
        self.res.append(track.copy())
        for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            track.append(nums[i])
            self.traverse(nums,i+1,track)
            track.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        track=[]
        nums.sort()
        self.traverse(nums,0,track)
        return self.res
