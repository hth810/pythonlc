class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        f=[[float('inf')]*(amount+1) for _ in range(n+1)]
        f[0][0]=0
        for i,x in enumerate(coins):
            for c in range(amount+1):
                if c<x:
                    f[i+1][c]=f[i][c]
                else:
                    f[i+1][c]=min(f[i][c],f[i+1][c-x]+1)
        ans=f[n][amount]
        return ans if ans<float('inf') else -1