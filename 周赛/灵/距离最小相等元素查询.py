from bisect import bisect_left
from collections import defaultdict


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n=len(nums)
        cnt=defaultdict(list)
        for i,c in enumerate(nums):
            cnt[c].append(i)
        for p in cnt.values():
            #前后补下标
            i0=p[0]
            p.insert(0,p[-1]-n)
            p.append(i0+n)
        for i,q in enumerate(queries):
            p=cnt[nums[q]]
            if len(p)==3:
                queries[i]=-1
            else:
                j=bisect_left(p,q)
                queries[i]=min(q-p[j-1],p[j+1]-q)
        return queries
