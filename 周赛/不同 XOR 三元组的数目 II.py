from itertools import combinations


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums=list(set(nums))
        st={x^y for x,y in combinations(nums,2)} | {0}
        return len({a^z for a in st for z in nums})