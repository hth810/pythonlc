from itertools import accumulate


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff=[0]*(n+1)
        for f,l,seat in bookings:
            diff[f]+=seat
            if l<n:
                diff[l+1]-=seat
        return list(accumulate(diff))[1:]