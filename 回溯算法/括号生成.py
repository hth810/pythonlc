class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m=n*2
        ans=[]
        path=['']*m
        def dfs(i,l):
            if i==m:
                ans.append(''.join(path))
                return
            if l<n:
                path[i]='('
                dfs(i+1,l+1)
            if i<l*2:
                path[i]=')'
                dfs(i+1,l)
        dfs(0,0)
        return ans