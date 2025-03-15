import math
from collections import defaultdict


class Solution:
    def is_prime(self,n):
        for i in range(2,math.isqrt(n)+1):
            if n%i==0:
                return False

        return n>=2
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        cnt=defaultdict(int)
        for i,row in enumerate(mat):
            for j,v in enumerate(row):
                for dx,dy in (0,1),(1,1),(1,0),(1,-1),(-1,1),(-1,-1),(0,-1),(-1,0):
                    x,y,value=i+dx,j+dy,v
                    while 0 <=x < m and 0 <= y < n:
                        value=value*10+mat[x][y]
                        if value in cnt or self.is_prime(value):
                            cnt[value]+=1

                        x+=dx
                        y+=dy
        ans,max_cnt=-1,0
        for i,c in cnt.items():
            if c>max_cnt:
                ans,max_cnt=i,c
            elif c==max_cnt:
                ans=max(ans,i)
        return ans