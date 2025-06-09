import heapq


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n=len(nums)
        queries.sort(key=lambda x:x[0])
        h=[]
        diff=[0]*(n+1)
        s=j=0
        for i,x in enumerate(nums):
            s+=diff[i]
            while j<len(queries) and queries[j][0]<=i:
                heapq.heappush(h,-queries[j][1])
                j+=1
            while s<x and h and -h[0]>=i:
                s+=1
                diff[-(heapq.heappop(h))+1]-=1
            if s<x:
                return -1
        return len(h)
