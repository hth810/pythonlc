import math
class Solution:
    def is_prime(self,m):
        for i in range(2,math.isqrt(m)+1):
            if m%i==0:
                return False
        return m>=2

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = 0
        for i, row in enumerate(nums):
            for x in row[i], row[-1 - i]:
                if x > ans and self.is_prime(x):
                    ans = x
        return ans

