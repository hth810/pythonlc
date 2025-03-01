class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a,b=len(word1),len(word2)
        @cache
        def dfs(word1,i,word2,j):
            if i==-1:
                return j+1
            if j==-1:
                return i+1
            if word1[i]==word2[j]:
                return dfs(word1,i-1,word2,j-1)
            else:
                return min(
                    dfs(word1,i,word2,j-1)+1,
                    dfs(word1,i-1,word2,j)+1,
                    dfs(word1,i-1,word2,j-1)+1
                )
        return dfs(word1,a-1,word2,b-1)


