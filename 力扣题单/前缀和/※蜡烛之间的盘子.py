class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n=len(s)
        candle=[-1]*n
        rig=[-1]*n
        plate=[0]*n
        if s[0]=='|':
            candle[0]=0
        if s[n-1]=='|':
            candle[n-1]=n-1
        for i in range(1,n):
            candle[i]=i if s[i]=='|' else candle[i-1]
        for i in range(n-2,-1,-1):
            rig[i]=i if s[i]=='|' else rig[i+1]
        for i in range(1,n):
            plate[i]=plate[i-1]+1 if s[i]=='*' else plate[i-1]
        ans=[]
        for low,up in queries:
            l=rig[low]
            r=candle[up]
            if l>=r or l==-1 or r==-1:
                ans.append(0)
            else:
                ans.append(plate[r]-plate[l])
        return ans
