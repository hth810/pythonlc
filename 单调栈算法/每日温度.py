class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[0]*n
        s=[]
        for i in range(n-1,-1,-1):
            while s and s[-1][0]<=temperatures[i]:
                s.pop()
            res[i]=0 if not s else (s[-1][-1]-i)
            s.append([temperatures[i],i])
        return res