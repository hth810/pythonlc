class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        from heapq import heappop,heappush
        ans,i=0,0
        h=[]
        while i<len(apples) or h:
            while h and h[0][0]==i:
                heappop(h)
            if i<len(apples) and apples[i]:
                heappush(h,[i+days[i],apples[i]])
            if h:
                ans+=1
                h[0][1]-=1
                if h[0][1]==0:
                    heappop(h)
            i+=1
        return ans