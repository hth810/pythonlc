class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n=len(cost)
        pre=[float('inf')]*(n+1)
        for i in range(1,n+1):
            pre[i]=min(pre[i-1],cost[i-1])
        return pre[1:]