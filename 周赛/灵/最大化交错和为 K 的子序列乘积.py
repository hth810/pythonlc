from functools import cache


class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        n=len(nums)
        mx=max(nums)
        ans=-1
        if k>=0:
            if k>(n+1)//2*mx:
                return -1
        else:
            if -k>n//2*mx:
                return -1
        @cache
        def dfs(i,s,m,op,emp):
            if m>limit or m<0:
                m=-1
            if i==n:
                if not emp and s==k:
                    nonlocal ans
                    ans=max(ans,m)
                return

            dfs(i+1,s,m,op,emp)
            x=nums[i]
            dfs(i+1,s+(-x if op else x),m*x,not op,False)

        dfs(0,0,1,False,True)
        return ans