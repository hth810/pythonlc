import math


class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def is_prime(m):
            for i in range(2, math.isqrt(m) + 1):
                if m % i == 0:
                    return False
            return m >= 2
        primes=set()
        n=len(s)
        for i in range(n):
            for j in range(i,n):
                a=s[i:j+1]
                a=int(a)
                if a>1 and is_prime(a):
                    primes.add(a)
        q=sorted(primes,reverse=True)
        if len(q)>=3:
            return sum(q[:3])
        else:
            return sum(q)