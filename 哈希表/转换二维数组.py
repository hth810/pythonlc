from collections import Counter


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt=Counter(nums)
        n=max(cnt.values())
        ans=[[] for _ in range(n)]
        for i,c in cnt.items():
            for j in range(c):
                ans[j].append(i)
        return ans