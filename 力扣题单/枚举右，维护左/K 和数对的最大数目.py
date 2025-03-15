from collections import defaultdict


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = defaultdict(int)
        for x in nums:
            if cnt[k - x]:
                cnt[k - x] -= 1
                ans += 1
            else:
                cnt[x] += 1
        return ans