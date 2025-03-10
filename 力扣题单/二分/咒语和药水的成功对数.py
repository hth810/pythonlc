from bisect import bisect_left


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n=len(potions)
        ans=[]
        for i in spells:
            t=success/i
            a=bisect_left(potions,t)
            ans.append(n-a)


        return ans
