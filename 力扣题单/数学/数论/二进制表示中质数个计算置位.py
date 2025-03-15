import math


class Solution:
    def is_prime(self,m):
        for i in range(2,math.isqrt(m)+1):
            if m%i==0:
                return False
        return m>=2

    def countPrimeSetBits(self, left: int, right: int) -> int:
        cnt=0
        for i in range(left,right+1):
            temp=str(bin(i))[2:]
            if self.is_prime(temp.count('1')):
                cnt+=1
        return cnt
