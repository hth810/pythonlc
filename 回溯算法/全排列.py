class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        path=[]
        used=[False]*n
        def dfs(i):
            if i==n:
                ans.append(path.copy())
                return
            for j,u in enumerate(used):
                if not u:
                    path.append(nums[j])
                    used[j]=True
                    dfs(i+1)
                    path.pop()
                    used[j]=False
        dfs(0)
        return ans