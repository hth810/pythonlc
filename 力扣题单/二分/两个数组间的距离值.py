from bisect import bisect_left


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans=0
        for i in arr1:
            a=bisect_left(arr2,i-d)
            if a==len(arr2) or arr2[a]-i>d:
                ans+=1

        return ans