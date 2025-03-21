from itertools import accumulate


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff=[0]*1001
        for pas,f,t in trips:
            diff[f]+=pas
            diff[t]-=pas
        return all(i<=capacity for i in accumulate(diff))