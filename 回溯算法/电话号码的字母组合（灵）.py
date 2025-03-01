

MAP=["","",'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)
        if n==0:
            return []
        ans=[]
        track=['']*n
        def dfs(i):
            if i==n:
                ans.append(''.join(track))
                return
            for c in MAP[int(digits[i])]:
                track[i]=c
                dfs(i+1)
        dfs(0)
        return ans



