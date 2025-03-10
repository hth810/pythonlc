class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_=prices[0]
        ans=0
        for a in prices:
            ans=max(ans,a-min_)
            min_=min(min_,a)
        return ans