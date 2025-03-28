class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1,stack2=[],[]
        for i,c in enumerate(s):
            if c=='#':
                if stack1:
                    stack1.pop()
                    continue
                continue
            stack1.append(c)
        for i,c in enumerate(t):
            if c=="#":
                if stack2:
                    stack2.pop()
                    continue
                continue
            stack2.append(c)
        return stack1==stack2
