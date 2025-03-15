from itertools import accumulate


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff=[0]*1001
        for pas,fro,to in trips:
            diff[fro]+=pas
            diff[to]-=pas
        return all(a<=capacity for a in accumulate(diff))