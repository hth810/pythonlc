class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        path=[]
        used=[False]*n
        def dfs(i):
            if i==n:
                ans.append(path.copy())
                return
            for j in range(n):
                if used[j]:
                    continue
                if j>0 and nums[j]==nums[j-1] and not used[j-1]:
                    continue
                path.append(nums[j])
                used[j]=True
                dfs(i+1)
                path.pop()
                used[j]=False

        dfs(0)
        return ans