class Solution:
    def resultingString(self, s: str) -> str:
        def check(a,b):
            return (ord(a)-ord(b))%26==1 or (ord(b)-ord(a))%26==1
        stack=[]
        for i in s:
            if stack and check(stack[-1],i):
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)