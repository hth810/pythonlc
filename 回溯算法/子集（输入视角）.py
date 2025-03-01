class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        path=[]
        def dfs(i):
            if i==n:
                res.append(path.copy())
                return

            dfs(i+1)

            path.append(nums[i])
            dfs(i+1)
            path.pop()

        dfs(0)
        return res