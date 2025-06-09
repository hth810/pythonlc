class Solution:
    def calculateScore(self, s: str) -> int:
        stack=[[] for _ in range(26)]
        ans=0
        for i,c in enumerate(s):
            c-=ord('a')
            if stack[25-c]:
                ans+=i-stack[25-c].pop()
            else:
                stack[c].append(i)
        return ans
