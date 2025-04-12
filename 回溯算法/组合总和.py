class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n=len(candidates)
        ans=[]
        path=[]
        def dfs(i,c):
            if c==0:
                ans.append(path.copy())
                return
            if c<0:
                return
            for j in range(i,-1,-1):
                if j<c:
                    path.append(candidates[j])
                    dfs(j,c-candidates[j])
                    path.pop()
        dfs(n-1,target)
        return ans
