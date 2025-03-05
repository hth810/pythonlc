class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m=n*2
        ans=[]
        path=['']*m
        def backtrack(i,open):
            if i==m:
                ans.append(''.join(path))
            if open<n:
                path[i]='('
                backtrack(i+1,open+1)
            if i<open*2:
                path[i]=')'
                backtrack(i+1,open)
        backtrack(0,0)
        return ans

