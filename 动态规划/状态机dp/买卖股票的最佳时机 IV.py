class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        f=[[-float('inf')]*2 for _ in range(k+2)]
        for j in range(1,k+2):
            f[j][0]=0
        for i,p in enumerate(prices):
            for j in range(k+1,0,-1):
                f[j+1][1]=max(f[j][1],f[j][0]-p)
                f[j+1][0]=max(f[j][0],f[j-1][1]+p)
        return f[k+1][0]
