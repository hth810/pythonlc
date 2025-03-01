class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums=[0]*1001
        diff=[0]*len(nums)

        for trip in trips:
            seat=trip[0]
            i=trip[1]
            j=trip[2]-1
            diff[i]+=seat
            if j+1<len((diff)):
                diff[j+1]-=seat
        for i in range(1,len(diff)):
            diff[i]+=diff[i-1]
        for i in range(len(diff)):
            if diff[i]>capacity:
                return False

        return True