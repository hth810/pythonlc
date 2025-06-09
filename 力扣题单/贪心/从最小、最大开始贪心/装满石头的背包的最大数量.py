class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        s=[]
        n=len(capacity)
        for i in range(n):
            s.append(capacity[i]-rocks[i])
        s.sort()
        flag=0
        for i,c in enumerate(s):
            additionalRocks-=c
            if additionalRocks<0:
                flag=1
                return 0 if i==0 else i
            elif additionalRocks==0:
                flag=1
                return i+1
        if not flag:
            return n