from functools import cache


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        f=[-1]*n
        @cache
        def dfs(i):
            res=0
            for j in range(i):
                if nums[i]%nums[j]:
                    continue
                temp=dfs(j)
                if temp>res:
                    res=temp
                    f[i]=j
            return res+1
        ml=mi=0
        for i in range(n):
            temp=dfs(i)
            if temp>ml:
                ml=temp
                mi=i
        path=[]
        i=mi
        while i>=0:
            path.append(nums[i])
            i=f[i]
        return path