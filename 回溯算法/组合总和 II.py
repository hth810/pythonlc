    class Solution:
        def __init__(self):
            self.res=[]
            self.sum=0

        def backtrack(self,candidates,start,track,target):
            if self.sum==target:
                self.res.append(track.copy())
                return
            if self.sum>target:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                track.append(candidates[i])
                self.sum+=candidates[i]
                self.backtrack(candidates,i+1,track,target)
                track.pop()
                self.sum-=candidates[i]
        def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            if not candidates:
                return self.res
            track=[]
            candidates.sort()
            self.backtrack(candidates,0,track,target)
            return self.res
