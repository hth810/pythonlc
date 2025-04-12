class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        def dfs(i,path):
            nonlocal res
            if i==n:
                res+=path
                return
            dfs(i+1,path)
            dfs(i+1,path^nums[i])
        dfs(0,0)
        return res
