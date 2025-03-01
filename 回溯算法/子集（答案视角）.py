class Solution:
    def __init__(self):
        self.res=[]

    def traverse(self,nums,start,track):
        self.res.append(track.copy())
        for i in range(start,len(nums)):
            track.append(nums[i])
            self.traverse(nums,i+1,track)
            track.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        track=[]
        self.traverse(nums,0,track)
        return self.res
