class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        temp=0
        ans=float('-inf')
        for i,c in enumerate(values):
            ans = max(ans, temp + c - i)
            temp=max(temp,i+c)
        return ans