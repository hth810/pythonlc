class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysNeed(capacity):
            load=0
            day=1
            i=0
            while i<len(weights):
                load+=weights[i]
                if load>capacity:
                    load=0
                    day+=1
                else:
                    i+=1
            return day
        left=max(weights)-1
        right=sum(weights)+1
        while left+1<right:
            mid=(left+right)//2
            loadDay=daysNeed(mid)
            if loadDay<=days:
                right=mid
            else:
                left=mid
        return right