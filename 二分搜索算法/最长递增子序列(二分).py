from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums):
        g=[]
        for x in nums:
            j=bisect_left(g,x)
            if j==len(g):
                g.append(x)
            else:
                g[j]=x
        return len(g)