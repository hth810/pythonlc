class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i,c in enumerate(s):
            if c=='*':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)