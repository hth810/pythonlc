class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n=len(words)
        pre=[0]*(n+1)
        temp=[0]*n
        ans=[]
        for i in range(n+1):
            if i<n:
                if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou':
                    temp[i]=1
            if i>=1:
                pre[i]=pre[i-1]+temp[i-1]
        for a,b in queries:
            ans.append(pre[b+1]-pre[a])

        return ans