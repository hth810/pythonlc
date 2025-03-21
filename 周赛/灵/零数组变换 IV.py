class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if all(x==0 for x in nums):
            return 0
        f=[[True]+[False]*x for x in nums]
        for k,(l,r,v) in enumerate(queries):
            for i in range(l,r+1):
                for j in range(nums[i],v-1,-1):
                    f[i][j]=f[i][j] or f[i][j-v]
            if all(fi[-1] for fi in f):
                return k+1
        return -1