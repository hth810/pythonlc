class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff=[0]*n
        for first,last,seats in bookings:
            diff[first-1]+=seats
            if last<n:
                diff[last]-=seats
        answer=[0]*n
        answer[0]=diff[0]
        for i in range(1,n):
            answer[i]=answer[i-1]+diff[i]
        return answer
