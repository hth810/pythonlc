class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return n
        a=len(str(bin(n)))-2
        return pow(2,a+1)
