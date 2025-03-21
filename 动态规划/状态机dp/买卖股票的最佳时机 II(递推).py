class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        f0,f1=0,float('-inf')
        for i in range(n):
            new_f0=max(f0,f1+prices[i])
            f1=max(f1,f0-prices[i])
            f0=new_f0
        return f0
