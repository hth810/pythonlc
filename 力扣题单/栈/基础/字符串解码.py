class Solution:
    def decodeString(self, s: str) -> str:
        n=len(s)
        i=0
        stack=[]
        x=0
        res=''
        for i in s:
            if i=='[':
                stack.append((x,res))
                x,res=0,''
            elif i==']':
                y,tmp=stack.pop()
                res=tmp+y*res
            elif '0'<=i<='9':
                x=x*10+int(i)
            else:
                res+=i
        return res