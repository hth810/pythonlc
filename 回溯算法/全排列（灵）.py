class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        path=[0]*n
        on_path=[False]*n
        def dfs(i):
            if i==n:
                ans.append(path.copy())
                return
            for j,c in enumerate(on_path):
                if not c:
                    path[i]=nums[j]
                    on_path[j]=True
                    dfs(i+1)
                    on_path[j]=False

        dfs(0)
        return ans