class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a,b=len(text1),len(text2)
        @cache
        def dfs(i,j):
            if i<0 or j<0:
                return 0
            if text1[i]==text2[j]:
                return dfs(i-1,j-1)+1
            else:
                return max(dfs(i-1,j),dfs(i,j-1))
        return dfs(a-1,b-1)